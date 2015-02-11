__author__ = 'mcdy143'
#!/usr/bin/python3

import os
import subprocess

inputDirectory = "/home/biol8803b/tmp/"
outputDirectory = "/home/biol8803b/assemblies/"
paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

fileHash = {}

#Generates a hashmap of 'key : value' pairs out of file names and paths.
def wranglePairedEnds(paths):
    for file in paths:
        newfile = ""
        if "R1" in file:
            newfile = file.replace("R1", "R*")
        elif "R2" in file:
            newfile = file.replace("R2", "R*")
        if not newfile in fileHash:
            fileHash[newfile] = [file]
        else:
            fileHash[newfile].append(file)
    return

def moduleedenaSE(file):
    base = os.path.basename(file)
    filename = os.path.splitext(base)[0]
    subprocess.call(["spades.py", "--careful", "-s", file, "-o", outputDirectory+filename+".spades",])

def moduleedenaPE(inputfileone, inputfiletwo):
    subprocess.call(["spades.py", "--careful", "-1", inputfileone, "-2", inputfiletwo, "-o", outputDirectory+ ])

for file in paths:

    moduleSpadesSE(file)
