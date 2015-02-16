__author__ = 'sungshine'
#!/usr/bin/python3
#Generates a hashmap of 'key : value' pairs where the file names are the keys and the values are the corresponding paths to single-end reads or paired end reads.

import os

inputDirectory = "/data/reads/" #raw reads
ODprinseq = "/home/sim8/assemblyMagicResults/prinseq/"
prinseqPaths = [os.path.join(ODprinseq,fn) for fn in next(os.walk(ODprinseq))[2]]

fileHash = {}

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

wranglePairedEnds(prinseqPaths)

print fileHash