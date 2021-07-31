import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from addondownloader import AddonDownloader
from pathlib import Path
class AddonManagerWindow(Gtk.Window):

    adl = None
    addons = ""
    addons_location = ""
    addons_location_field = None
    addon_link_textview = None
    layout_box = None
    start_download_button = None
    status_label = None

    def __init__(self):
        super().__init__(title="ESO Addon Manager for Linux")
        self.create_addon_files()

        self.set_size_request(300, 500)
        self.timeout_id = None

        self.create_layout_box()
        self.create_addon_location_field()
        self.create_addon_link_textview()
        self.create_download_button()
        self.create_status_label()

        self.adl = AddonDownloader(self.status_label)

    def create_layout_box(self):
        self.layout_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)
        self.add(self.layout_box)

    def create_addon_location_field(self): 
        label = Gtk.Label(label="ESO Addon folder location")
        label.set_line_wrap(True)
        self.addons_location_field = Gtk.Entry()
        self.addons_location_field.set_text(self.addons_location)
        self.layout_box.pack_start(label, False, False, 0)
        self.layout_box.pack_start(self.addons_location_field, False, False, 10)

    def create_addon_link_textview(self):
        label = Gtk.Label(label="Links to ESOUI.com addon pages")
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

        try:
            self.adl.start()
        except Exception as err:
            self.status_label.set_text(str(err))



