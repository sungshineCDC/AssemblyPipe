__author__ = 'mcdy143'
#!/usr/bin/python3

import os
import subprocess

inputDirectory = "/home/sim8/assemblyMagicResults/prinseq/"
outputDirectory = "/home/sim8/assemblyMagicResults/edena/"
paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

fileHash = {}

#Generates a hashmap of 'key : value' pairs out of file names and paths.
def wranglePairedEnds(paths):
    for file in paths:
        print file
        newfile = ""
        if "R1" in file:
            newfile = file.replace("R1", "R*")
            print "newFile, R1 --", newfile
        elif "R2" in file:
            newfile = file.replace("R2", "R*")
            print "newFile, R2 --", newfile
        if not newfile in fileHash:
            print "newFile, notin --", newfile
            fileHash[newfile] = [file]
        else:
            print "already in newfile --", newfile
            fileHash[newfile].append(file)
    return

def moduleedenaSE(file):
    base = os.path.basename(file)
    filename = os.path.splitext(base)[0]
    fileOutputDirectory = outputDirectory+str(filename)
    subprocess.call(["mkdir", fileOutputDirectory])
    subprocess.call(["edena", "-r", file, "-p", fileOutputDirectory+"/out"])
    subprocess.call(["edena", "-e", fileOutputDirectory+"/out.ovl", "-p", fileOutputDirectory+"/"])

def moduleedenaPE(inputfileone, inputfiletwo):
    subprocess.call(["spades.py", "--careful", "-1", inputfileone, "-2", inputfiletwo, "-o", outputDirectory])

for file in paths[:2]:
    moduleedenaSE(file)
