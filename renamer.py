# Python3
# This file is used to clean up, rename, and unzip assignments downloaded from D2L.
# The user just needs to unzip the main zip file (and probably rename it).
# Run python3 renamer.py
# The user will be prompted for the folder name.
# The script will delete the index.html file from D2L,
# rename all of the student files, and unzip the .zips 

# TO DO - add unzip for the initial zip file
# TO DO - add .rar handling

import os
from os import walk
import zipfile

#Ask user for the name of the folder containing the student zips
input = input("What is the name of the folder?")

#assignments folder
folder = "../" + input + "/"

def getFiles(folder):
    #Get all files
    f = []
    for (dirpath, dirnames, filenames) in walk(folder):
        f.extend(filenames) #add the LIST of filenames to f
        break
    return f

f = getFiles(folder)

#for each file
for e in f:
    #delete index.html
    print(f)
    if e == "index.html":
        os.remove(folder + e)

    oldFilename = folder + e

    #if filename has multiple parts
    if len(e.split("- ")) > 1:
        #split filename down to student name
        name = e.split("- ") #get student name
        name = name[1].split(" ")
        type = e.split(".") #get file type
        #construct new filename
        newFilename = folder + name[0] + name[1] + "." + type[1]

        #save file with new name
        try:
            os.rename(oldFilename, newFilename)
        except FileExistsError:
            print(newFilename + " Exists")

#get new list of files
f = getFiles(folder)
#if ends in .zip, then unzip, else do nothing
for e in f:
    if e.split(".")[1] == "zip":
        os.mkdir(folder + e.split(".")[0])
        #unzip
        with zipfile.ZipFile(folder + e, "r") as zf:
            zf.extractall(folder + e.split(".")[0])
        os.remove(folder + e)