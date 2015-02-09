__author__ = 'sungshine'
#!/usr/bin/python3
#assemblyMagic Pipeline

import os
import sys
import subprocess

inputDirectory = sys.argv[1]    #/home/biol8803b/data
outputDirectory = sys.argv[2]   #/home/biol8803b/preProcessed
paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

fileHash = {}

#Generates a hashmap of 'key : value' pairs.
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

#Takes STDIN for variables inputDirectory & outputDirectory, and creates the outputDirectory.
def makeOutDirectory(outputDirectory):
    if not os.path.exists(outputDirectory):
        os.makedirs(outputDirectory)

#Invokes fastqc on raw read files passing in the files in as an argument.
def moduleFastQC(file, outputDirectory):
    subprocess.call(['fastqc', "-o", outputDirectory, file,])

#Invokes prinseq-lite on raw read files using default settings passing files in as argument.
def modulePrinseq(file):
    subprocess.call(['prinseq-lite', '-verbose', '-fastq',file,'-out_format','3', '-out_good', outputDirectory, '-out_bad', ouputDirectory,])

#Preprocess module, sets up directories and
def preProcess(paths):
    for file in paths:
        moduleFastQC(file)
        modulePrinseq(file)


####################################################################
###                         MAIN PROGRAM                         ###
####################################################################

makeOutDirectory(outputDirectory)
preProcess(paths)
wranglePairedEnds(paths)

# for keys in fileHash:
#
#     if fileHash.values() == 2
#
#         invoke moduleSPAdes with paired-end flags
#
#     elif fileHash.values() == 1
#
#         invoke moduleSPAdes with single-end flags