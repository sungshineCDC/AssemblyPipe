__author__ = 'mcdy143, sungshine'
#!/usr/bin/env python

import os
import subprocess

def wranglePairedEnds(prinseqPaths):
    for file in prinseqPaths:
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

def moduleedenaSE(inputfileOne):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    fileOutputDirectory = ODedena+str(filename)
    subprocess.call(["mkdir", fileOutputDirectory])
    subprocess.call(["edena", "-r", inputfileOne, "-p", fileOutputDirectory+"/out"])
    subprocess.call(["edena", "-e", fileOutputDirectory+"/out.ovl", "-p", fileOutputDirectory+"/"])

def moduleedenaPE(inputfileOne, inputfileTwo):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    fileOutputDirectory = ODedena+str(filename)
    subprocess.call(["mkdir", fileOutputDirectory])
    subprocess.call(["edena", "-DRpairs", inputfileOne, inputfileTwo, "-p", fileOutputDirectory+"/out"])
    subprocess.call(["edena", "-e", fileOutputDirectory+"/out.ovl", "-p", fileOutputDirectory+"/"])

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
        moduleedenaPE(inputfileOne, inputfileTwo)

