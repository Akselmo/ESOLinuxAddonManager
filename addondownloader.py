
import re, shutil, os, re, zipfile
from urllib.request import urlopen, Request

class AddonDownloader():

    file_number = 0

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

    addons = ""
    addons_location = ""
    addon_temp_folder = "addontemp"
    addon_temp_name = "addon{0}.zip"
    status = None
    buttons = []

    def __init__(self, status, buttons):
        self.status = status
        self.buttons = buttons
        addons_file = open("addons.txt", "r")
        addons_location_file = open("addonslocation.txt", "r")
        self.addons = addons_file.read()
        self.addons_location = addons_location_file.read()

    def start(self):
        self.toggle_button_sensitivity(False)
        self.status.set_text("Starting....")
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
        self.toggle_button_sensitivity(False)
        self.status.set_text("Updating TTC...")
        target_location = self.addons_location+"/TamrielTradeCentre/"
        print(target_location)
        if os.path.isdir(self.addon_temp_folder) == False:
            os.mkdir(self.addon_temp_folder)
        self.file_number = 0
        link = "https://"+ttc_region+".tamrieltradecentre.com/download/PriceTable"
        file = self.download(link, self.file_number, custom_url=link)
        self.unzip(file, custom_location=target_location)
        shutil.rmtree(self.addon_temp_folder)
        self.status.set_text("Done! Updated TTC pricetables to " + target_location)
        self.toggle_button_sensitivity(True)

    def download(self, link, file_number, custom_url=""):
        self.status.set_text("Downloading: " + link)
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
        self.status.set_text("Unzipping: " + file)
        with zipfile.ZipFile(file, 'r') as z:
            if custom_location == "":
                z.extractall(self.addons_location)
            else:
                z.extractall(custom_location)

    def end(self):
        self.status.set_text("Done! Addons downloaded and unzipped to " + self.addons_location)
        self.toggle_button_sensitivity(True)

    def toggle_button_sensitivity(self, sensitivity):
        for button in self.buttons:
            button.set_sensitive(sensitivity)
