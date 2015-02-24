__author__ = 'sungshine'
#!/usr/bin/python3
import os

#Generates dictionary of paired-end file path(s). Prints the dictionary.

inputDirectory = sys.argv[1]    #Takes as STDIN, path to directory of trimmed reads
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

wranglePairedEnds(prinseqPaths)

for key, filepath in fileHash.iteritems() :
    print key, filepath
