import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from addonmanager import AddonManagerWindow

if __name__ == "__main__":
    win = AddonManagerWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
