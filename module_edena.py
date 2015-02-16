__author__ = 'mcdy143'
#!/usr/bin/python3

import os
import subprocess

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

def moduleedenaSE(inputfileOne):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[1]
    fileOutputDirectory = ODedena+str(filename)
    subprocess.call(["mkdir", fileOutputDirectory])
    subprocess.call(["edena", "-r", inputfileOne, "-p", fileOutputDirectory+"/out"])
    subprocess.call(["edena", "-e", fileOutputDirectory+"/out.ovl", "-p", fileOutputDirectory+".edena"])

def moduleedenaPE(inputfileOne, inputfileTwo):
    base = os.path.basename(inputfileone)
    filename = os.path.splitext(base)[1]
    fileOutputDirectory = ODedena+str(filename)
    subprocess.call(["mkdir", fileOutputDirectory])
    subprocess.call(["edena", "-DRpairs", inputfileOne, inputfileTwo, "-p", fileOutputDirectory+"/out"])
    subprocess.call(["edena", "-e", fileOutputDirectory+"/out.ovl", "-p", fileOutputDirectory+".edena"])

########################################################################################################################

inputDirectory = "/home/sim8/test.data/"
outputDirectory = "/home/sim8/assemblyMagicResults/"

ODerrors = "/home/sim8/assemblyMagicResults/errors/"
ODprinseq = "/home/sim8/assemblyMagicResults/prinseq/"
ODfastqc = "/home/sim8/assemblyMagicResults/fastQCresults/"
ODedena = "/home/sim8/assemblyMagicResults/edena/"

fileHash = {}

paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

# preProcess(paths)

prinseqPaths = [os.path.join(ODprinseq,fn) for fn in next(os.walk(ODprinseq))[2]]

wranglePairedEnds(prinseqPaths)

inputfileOne = ""
inputfileTwo = ""

for key in fileHash:

    hashValues = fileHash.get(key)
    sortedValues = sorted(hashValues)

    if len(sortedValues) == 1:
        inputfileOne = sortedValues[0]
        moduleedenaSE(inputfileOne)

    if len(sortedValues) == 2:
        inputfileOne = sortedValues[0]
        inputfileTwo = sortedValues[1]
        moduleedenaSE(inputfileOne)

#This code is working