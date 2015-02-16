__author__ = 'sungshine'
#!/usr/bin/python3

import os
import subprocess

def wranglePairedEnds(prinseqPaths):

    for file in prinseqPaths:
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

def moduleSpadesSE(inputfileOne):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    subprocess.call(["spades.py", "--careful", "-s", inputfileOne, "-o", ODspades+filename+".spades",])

def moduleSpadesPE(inputfileOne, inputfileTwo):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    subprocess.call(["spades.py", "--careful", "-1", inputfileOne, "-2", inputfileTwo, "-o", ODspades+filename+".spades",])

########################################################################################################################

inputDirectory = "/data/reads/"     #raw reads
ODprinseq = "/home/sim8/assemblyMagicResults/prinseq/"
prinseqPaths = [os.path.join(ODprinseq,fn) for fn in next(os.walk(ODprinseq))[2]]

fileHash = {}
wranglePairedEnds(prinseqPaths)

for key in fileHash:

    currentValue = fileHash.get(key)
    sortedValue = sorted(currentValue)

    #call assemblers to execute single-end read
    if len(sortedValue) == 1:
        inputfileOne = sortedValue[0]
        moduleSpadesSE(inputfileOne)

    #execute paired-end reads
    if len(sortedValue) == 2:
        inputfileOne = sortedValue[0]
        inputfileTwo = sortedValue[1]
        moduleSpadesPE(inputfileOne, inputfileTwo)