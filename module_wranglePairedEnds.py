__author__ = 'sungshine'
#!/usr/bin/env python
import os

#Returns a dictionary of 'key : value' pairs.
#Keys return the isolate identification numbers.
#Values return the file path(s) to the raw read file(s).

def wranglePairedEnds(paths):
    for file in paths:
        newfile = ""
        if "R1" in file:
            newfile = file.replace("R1", "R*")  #make the key/file ambiguous
        elif "R2" in file:
            newfile = file.replace("R2", "R*")
        if not newfile in fileHash:
            fileHash[newfile] = [file]
        else:
            fileHash[newfile].append(file)
    return

paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]    #store file path(s) in list
fileHash = {}
wranglePairedEnds(paths)
print fileHash