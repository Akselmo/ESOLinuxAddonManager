import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject
from addonmanager import AddonManagerWindow
GObject.threads_init()

if __name__ == "__main__":
    win = AddonManagerWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
