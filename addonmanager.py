from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QMessageBox,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QStyle,
    QFileDialog,
    QTextEdit,
)
from PySide6 import QtGui
from PySide6.QtCore import QStandardPaths, QUrl, QFile, QSaveFile, QDir, QIODevice, Slot
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager
import sys, re, shutil, os

class AddonManager(QWidget):
    addon_temp_folder = "addontemp"
    addon_temp = "./addontemp/addon"
    addon_file = "addons.txt"
    addons_location_file = "addonslocation.txt"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.manager = QNetworkAccessManager(self)
        #set window title
        self.setWindowTitle("ESO Addon Manager for Linux")
        #create ui items
        self.addon_link_box = QTextEdit()
        self.addon_folder = QLineEdit()

        self.progress_bar = QProgressBar()

        self.save_settings_buton = QPushButton("Save settings")
        self.download_button = QPushButton("Download addons")
        
        self.addon_link_box.setPlaceholderText("Paste links to addons/libraries here, one per line")

        #  Current QFile
        self.file = None
        # Current QNetworkReply
        self.reply = None

        self.addon_folder.setPlaceholderText("Select your ESO addon folder")
        
        #open folder action
        self._open_folder_action = self.addon_folder.addAction(
            QApplication.style().standardIcon(QStyle.SP_DirOpenIcon), QLineEdit.TrailingPosition
        )
        self._open_folder_action.triggered.connect(self.open_folder)

        self.set_colors()
        self.make_layout()

        self.download_button.clicked.connect(self.start_addon_manager)

    def set_colors(self):
        pal = self.palette()
        text_color = QtGui.QColor("green")
        pal.setColor(QtGui.QPalette.PlaceholderText, text_color)
        self.setPalette(pal)

    def make_layout(self):
        #buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.save_settings_buton)
        buttons_layout.addWidget(self.download_button)

        #main
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.addon_link_box)
        main_layout.addWidget(self.addon_folder)
        main_layout.addWidget(self.progress_bar)
        main_layout.addStretch()

        main_layout.addLayout(buttons_layout)

        self.resize(500,300)

    @Slot()
    def start_addon_manager(self):
        if os.path.isdir(self.addon_temp_folder) == False:
            os.mkdir(self.addon_temp_folder)
        links = self.addon_link_box.toPlainText().split("\n")
        i = 0
        for link in links:
            self.start_download(link, i)
            self.unzip_and_move(i)
            i += 1
        shutil.rmtree(self.addon_temp_folder)



    @Slot()
    def start_download(self, link, i):
        tempfilename = self.addon_temp+str(i)+".zip"
        info = re.findall("https://www.esoui.com/downloads/info(\d*)", link)[0]
        download_url = QUrl("https://cdn.esoui.com/downloads/file" + info + "/")
        dest_file = QDir(tempfilename).filePath(download_url.fileName())
        #create the temp file which we will overwrite with correct data
        try:
            file = open(tempfilename,"x")
            file.close()
        except:
            print("File already exists, moving on")

        self.download_button.setDisabled(True)
        # Create the file in write mode to append bytes
        self.file = QSaveFile(dest_file)
        if self.file.open(QIODevice.WriteOnly):
        #Start a GET HTTP request
            self.reply = self.manager.get(QNetworkRequest(download_url))
            self.reply.downloadProgress.connect(self.on_progress)
            self.reply.finished.connect(self.on_finished)
            self.reply.readyRead.connect(self.on_ready_read)
            self.reply.errorOccurred.connect(self.on_error)
        else:
            error = self.file.errorString()
            print(f"Cannot open device: {error}")
    

    @Slot()
    def unzip_and_move(self, i):
        tempfilename = self.addon_temp+str(i)+".zip"
        addon_path = QDir.fromNativeSeparators(self.addon_folder.text().strip())
        print(addon_path)
        print(tempfilename)


    @Slot()
    def open_folder(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Open ESO Addons folder", QDir.homePath(), QFileDialog.ShowDirsOnly)

        if dir_path:
            dest_dir = QDir(dir_path)
            self.addon_folder.setText(QDir.fromNativeSeparators(dest_dir.path()))

    @Slot(int, int)
    def on_progress(self, bytesReceived: int, bytesTotal: int):
        self.progress_bar.setRange(0, bytesTotal)
        self.progress_bar.setValue(bytesReceived)

    @Slot(QNetworkReply.NetworkError)
    def on_error(self, code: QNetworkReply.NetworkError):
        """ Show a message if an error happen """
        if self.reply:
            QMessageBox.warning(self, "Error Occurred", self.reply.errorString())

    @Slot()
    def on_ready_read(self):
        """ Get available bytes and store them into the file"""
        if self.reply:
            if self.reply.error() == QNetworkReply.NoError:
                self.file.write(self.reply.readAll())

    @Slot()
    def on_finished(self):
        """ Commit the file and close """
        if self.file:
            self.file.commit()

        self.download_button.setDisabled(False)