from pickBackground import BackgroundPicker
import os
Picker = BackgroundPicker()

file = str(Picker.pickRandomBackground())
Picker.moveFile(file)

fullPath = "/home/toor/BackgroundChanger/BackgroundChanger/current_wallpaper/"+file[5:]

command = "gsettings set org.gnome.desktop.background picture-uri file:///" + fullPath

os.system(command)
