from pathlib import Path
import os
import sys
import random
import shutil
import glob

class BackgroundPicker:
    def pickRandomBackground(self):
        top = "data/"
        ext = "jpg"
        file_list = list(Path(top).glob(f"**/*.{ext}"))
        if not len(file_list):
            return None
        return file_list[random.randint(0, len(file_list)-1)]
    def clearDirectory(self):
        shutil.rmtree("current_wallpaper/")
        os.makedirs("current_wallpaper/")
    def moveFile(self, filename):
        self.clearDirectory()
        shutil.copy2(filename, "current_wallpaper/")
    
