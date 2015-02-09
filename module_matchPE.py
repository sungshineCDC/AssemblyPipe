__author__ = 'sungshine '
#!/usr/bin/python3
#Generates a hashmap of 'key : value' pairs where the file names are the keys and the values are the corresponding paths to single-end reads or paired end reads.

import os

inputDirectory = "/Users/sungshine/Test/"
paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

fileHash = {}

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

wranglePairedEnds(paths)

print fileHash