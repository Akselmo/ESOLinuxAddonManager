import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GLib
import re, shutil, os, re, zipfile, time, certifi, ssl
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
        
    def start(self):
        self.refresh_addon_location()
        GLib.idle_add(self.set_button_sensitivity, False)
        self.set_status_text("Starting....")
        if os.path.isdir(self.addon_temp_folder) == False:
            os.mkdir(self.addon_temp_folder)
        links = self.addons.split("\n")
        self.file_number = 0
        for link in links:
            info = re.findall("https://www.esoui.com/downloads/info(\d*)", link)[0]
            download_url = "https://cdn.esoui.com/downloads/file" + info + "/1"
            file = self.download(self.file_number, download_url)
            if file == False:
                print("Failed to use the new url, using old url instead...")
                download_url = "https://cdn.esoui.com/downloads/file" + info + "/"
                file = self.download(self.file_number, download_url)
            self.unzip(file)
            self.file_number += 1
        #delete temp folder
        shutil.rmtree(self.addon_temp_folder)
        self.end()

    def start_ttc_update(self, ttc_region):
        self.refresh_addon_location()
        GLib.idle_add(self.set_button_sensitivity, False)
        self.set_status_text("Updating TTC...")
        target_location = self.addons_location+"/TamrielTradeCentre/"
        if os.path.isdir(self.addon_temp_folder) == False:
            os.mkdir(self.addon_temp_folder)
        self.file_number = 0
        download_url = "https://"+ttc_region+".tamrieltradecentre.com/download/PriceTable"
        file = self.download(self.file_number, download_url)
        self.unzip(file, custom_location=target_location)
        shutil.rmtree(self.addon_temp_folder)
        self.set_status_text("Done! Updated TTC pricetables to " + target_location)
        self.end()

    def download(self, file_number, download_url):
        self.set_status_text("Downloading: " + download_url)
        tempfilename = self.addon_temp_folder + "/" + self.addon_temp_name.format(str(file_number))
        request = Request(url=download_url, headers=self.headers)
        ssl._create_default_https_context = ssl._create_unverified_context
        if urlopen(request, cafile=certifi.where()).getcode() != 200:
            return False
        response = urlopen(request, cafile=certifi.where())
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
    
    def refresh_addon_location(self):
        addons_file = open("addons.txt", "r")
        addons_location_file = open("addonslocation.txt", "r")
        self.addons = addons_file.read()
        self.addons_location = addons_location_file.read()

    def end(self):
        self.set_status_text("Done! Addons downloaded and unzipped to " + self.addons_location)
        GLib.idle_add(self.set_button_sensitivity, True)

