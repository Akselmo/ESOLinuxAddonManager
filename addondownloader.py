
import sys, re, shutil, os, re, zipfile
from urllib.request import urlopen, Request

class AddonDownloader():
    
    file_number = 0

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

    addons = ""
    addons_location = ""
    addon_temp_folder = "addontemp"
    addon_temp_name = "addon{0}.zip"

    def __init__(self):
        try:
            addons_file = open("addons.txt", "r")
            addons_location_file = open("addonslocation.txt", "r")
            self.addons = addons_file.read()
            self.addons_location = addons_location_file.read()
        except:
            print("FAIL: One or both addon text files were empty or not found!")
            print("Check addons.txt and addonslocation.txt")
            return



    def start(self):
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

    def download(self, link, file_number):
        tempfilename = self.addon_temp_folder + "/" + self.addon_temp_name.format(str(file_number))
        info = re.findall("https://www.esoui.com/downloads/info(\d*)", link)[0]
        download_url = "https://cdn.esoui.com/downloads/file" + info + "/"
        print(download_url)
        request = Request(url=download_url, headers=self.headers)
        response = urlopen(request)
        with open(tempfilename, "wb") as f:
            f.write(response.read())
        return tempfilename
    
    def unzip(self, file):
        with zipfile.ZipFile(file, 'r') as z:
            z.extractall(self.addons_location)
    
    def end(self):
        print("Addons downloaded and unzipped to " + self.addons_location)


if __name__ == "__main__":
    addon = AddonDownloader()
    addon.start()