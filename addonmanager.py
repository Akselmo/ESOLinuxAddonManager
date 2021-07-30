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
import sys

class AddonManager(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        #set window title
        self.setWindowTitle("ESO Addon Manager for Linux")
        #create ui items
        self.addon_link_box = QTextEdit()
        self.addon_folder = QLineEdit()

        self.progress_bar = QProgressBar()

        self.save_settings_buton = QPushButton("Save settings")
        self.download_button = QPushButton("Download addons")
        self.stop_button = QPushButton("Stop")
        
        self.addon_link_box.setPlaceholderText("Paste links to addons/libraries here, one per line")

        self.addon_folder.setPlaceholderText("Select your ESO addon folder")
        
        #open folder action
        self._open_folder_action = self.addon_folder.addAction(
            QApplication.style().standardIcon(QStyle.SP_DirOpenIcon), QLineEdit.TrailingPosition
        )
        self._open_folder_action.triggered.connect(self.open_folder)

        self.set_colors()
        self.make_layout()

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
        buttons_layout.addWidget(self.stop_button)

        #main
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.addon_link_box)
        main_layout.addWidget(self.addon_folder)
        main_layout.addWidget(self.progress_bar)
        main_layout.addStretch()

        main_layout.addLayout(buttons_layout)

        self.resize(500,300)



    @Slot()
    def open_folder(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Open ESO Addons folder", QDir.homePath(), QFileDialog.ShowDirsOnly)

        if dir_path:
            dest_dir = QDir(dir_path)
            self.addon_folder.setText(QDir.fromNativeSeparators(dest_dir.path()))