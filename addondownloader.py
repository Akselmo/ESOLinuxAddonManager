import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GLib
import re, shutil, os, re, zipfile, time
from urllib.request import urlopen, Request

class AddonDownloader():

    file_number = 0

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

    addons = ""
    addons_location = ""
    addon_temp_folder = "addontemp"
    addon_temp_name = "addon{0}.zip"

    #GUI functions
    set_status_text = None

    def __init__(self, func_set_button_sensitivity, func_set_status_text):
        self.set_button_sensitivity = func_set_button_sensitivity
        self.set_status_text = func_set_status_text
        addons_file = open("addons.txt", "r")
        addons_location_file = open("addonslocation.txt", "r")
        self.addons = addons_file.read()
        self.addons_location = addons_location_file.read()

    def start(self):
        GLib.idle_add(self.set_button_sensitivity, False)
        self.set_status_text("Starting....")
        if os.path.isdir(self.addon_temp_folder) == False:
            os.mkdir(self.addon_temp_folder)
        links = self.addons.split("\n")
        self.file_number = 0
        for link in links:
            file = self.download(link, self.file_number)
            self.unzip(file)
            self.file_number += 1
        #delete temp folder
        shutil.rmtree(self.addon_temp_folder)
        self.end()

    def start_ttc_update(self, ttc_region):
        GLib.idle_add(self.set_button_sensitivity, False)
        self.set_status_text("Updating TTC...")
        target_location = self.addons_location+"/TamrielTradeCentre/"
        if os.path.isdir(self.addon_temp_folder) == False:
            os.mkdir(self.addon_temp_folder)
        self.file_number = 0
        link = "https://"+ttc_region+".tamrieltradecentre.com/download/PriceTable"
        file = self.download(link, self.file_number, custom_url=link)
        self.unzip(file, custom_location=target_location)
        shutil.rmtree(self.addon_temp_folder)
        self.set_status_text("Done! Updated TTC pricetables to " + target_location)

    def download(self, link, file_number, custom_url=""):
        self.set_status_text("Downloading: " + link)
        tempfilename = self.addon_temp_folder + "/" + self.addon_temp_name.format(str(file_number))
        if custom_url == "":
            info = re.findall("https://www.esoui.com/downloads/info(\d*)", link)[0]
            download_url = "https://cdn.esoui.com/downloads/file" + info + "/"
        else:
            download_url = custom_url
        request = Request(url=download_url, headers=self.headers)
        response = urlopen(request)
        with open(tempfilename, "wb") as f:
            f.write(response.read())
        return tempfilename

    def unzip(self, file, custom_location=""):
        self.set_status_text("Unzipping: " + file)
        with zipfile.ZipFile(file, 'r') as z:
            if custom_location == "":
                z.extractall(self.addons_location)
            else:
                z.extractall(custom_location)

    def end(self):
        self.set_status_text("Done! Addons downloaded and unzipped to " + self.addons_location)
        GLib.idle_add(self.set_button_sensitivity, True)





