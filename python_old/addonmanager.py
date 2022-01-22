import gi
gi.require_version("Gtk", "3.0")
import gi
from gi.repository import Gtk, GObject
from addondownloader import AddonDownloader
from pathlib import Path
from threading import Thread
class AddonManagerWindow(Gtk.Window):

    adl = None
    addons = ""
    addons_location = ""
    addons_location_field = None
    addon_link_textview = None
    layout_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)
    start_download_button = None
    update_ttc_button = None
    ttc_eu_radiobutton = None
    ttc_us_radiobutton = None
    status_label = None
    buttons = []
    ttc_region = "eu"

    def __init__(self):
        GObject.threads_init()
        super().__init__(title="ESO Addon Manager for Linux")
        self.create_addon_files()
        self.set_size_request(400, 500)
        self.timeout_id = None
        self.add(self.layout_box)
        self.create_addon_location_field()
        self.create_addon_link_textview()
        self.create_download_button()
        self.create_ttc_radio_buttons()
        self.create_download_ttc_button()
        self.create_status_label()
        self.buttons = [self.start_download_button, self.update_ttc_button]
        self.adl = AddonDownloader(self.update_buttons, self.update_status_text)

    def create_addon_location_field(self):
        label = Gtk.Label(label="ESO Addon folder location")
        label.set_line_wrap(True)
        self.addons_location_field = Gtk.Entry()
        self.addons_location_field.set_text(self.addons_location)
        self.layout_box.pack_start(label, False, False, 0)
        self.layout_box.pack_start(self.addons_location_field, False, False, 10)

    def create_addon_link_textview(self):
        label = Gtk.Label(label="Links to ESOUI.com addon pages, one per line")
        label.set_line_wrap(True)
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.layout_box.pack_start(label, False, False, 0)
        self.layout_box.pack_start(scrolledwindow, True, True, 10)

        self.addon_link_textview = Gtk.TextView()
        self.textbuffer = self.addon_link_textview.get_buffer()
        self.textbuffer.set_text(self.addons)
        scrolledwindow.add(self.addon_link_textview)

    def create_download_button(self):
        self.start_download_button = Gtk.Button(label="Download")
        self.start_download_button.connect("clicked", self.on_start_download)
        self.layout_box.pack_start(self.start_download_button, False, False, 0)

    def create_download_ttc_button(self):
        self.update_ttc_button = Gtk.Button(label="Update TTC")
        self.update_ttc_button.connect("clicked", self.on_start_ttc_update)
        self.layout_box.pack_start(self.update_ttc_button, False, False, 0)

    def create_status_label(self):
        self.status_label = Gtk.Label(label="Ready to download...")
        self.status_label.set_line_wrap(True)
        self.layout_box.pack_start(self.status_label, False, False, 0)

    def create_addon_files(self):
        addons_file = open(self.touch_file("addons.txt"), "r+")
        addons_location_file = open(self.touch_file("addonslocation.txt"), "r+")
        self.addons = addons_file.read()
        self.addons_location = addons_location_file.read()
        addons_file.close()
        addons_location_file.close()

    def touch_file(self, filename):
        """Makes sure file exists"""
        filename = Path(filename)
        filename.touch(exist_ok=True)
        return filename

    def create_ttc_radio_buttons(self):
        self.ttc_eu_radiobutton = Gtk.RadioButton.new_with_label_from_widget(None, "EU")
        self.ttc_eu_radiobutton.connect("toggled", self.on_ttc_radio_button_toggled, "eu")
        self.layout_box.pack_start(self.ttc_eu_radiobutton, False, False, 0)

        self.ttc_us_radiobutton = Gtk.RadioButton.new_with_label_from_widget(self.ttc_eu_radiobutton, "US")
        self.ttc_us_radiobutton.connect("toggled", self.on_ttc_radio_button_toggled, "us")
        self.layout_box.pack_start(self.ttc_us_radiobutton, False, False, 0)

    def on_ttc_radio_button_toggled(self, button, name):
        self.ttc_region = name

    def update_buttons(self, sensitivity):
        for button in self.buttons:
            button.set_sensitive(sensitivity)

    def update_status_text(self, text):
        self.status_label.set_text(text)

    def on_start_ttc_update(self, widget):
        addons_location_file = open("addonslocation.txt", "w")
        addons_location_file.write(self.addons_location_field.get_text())
        addons_location_file.close()
        adlthread = Thread(target=self.adl.start_ttc_update, args=(self.ttc_region,))
        self.handle_thread(adlthread)


    def on_start_download(self, widget):
        #Save all the input data to text files
        #ESO addon location folder
        addons_location_file = open("addonslocation.txt", "w")
        addons_location_file.write(self.addons_location_field.get_text())
        addons_location_file.close()
        #List of links
        addons = open("addons.txt", "w")
        textbuffer = self.addon_link_textview.get_buffer()
        start_iter = textbuffer.get_start_iter()
        end_iter = textbuffer.get_end_iter()
        links = textbuffer.get_text(start_iter, end_iter, True)
        addons.write(links.rstrip("\n"))
        addons.close()

        adlthread = Thread(target=self.adl.start)
        self.handle_thread(adlthread)

    def handle_thread(self, thread):
        thread.daemon = True
        try:
            self.update_buttons(False)
            thread.start()
            self.update_buttons(True)
        except Exception as err:
            self.update_status_text(str(err))
            self.update_buttons(True)

