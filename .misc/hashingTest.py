__author__ = 'sungshine'
#!/usr/bin/python3
#assemblyMagic Pipeline

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

def moduleFastQC(file):
    subprocess.call(['fastqc', "-o", ODfastqc, file,])

def modulePrinseq(file):
    base = os.path.basename(file)
    filename = os.path.splitext(base)[0]
    subprocess.call(['prinseq-lite', '-verbose', '-fastq', file, '-out_format','3', '-out_good', ODprinseq+filename+".prinseq", "-out_bad", ODerrors+filename+".bad.prinseq",])

def preProcess(paths):
    for file in paths:
        moduleFastQC(file)
        modulePrinseq(file)


###############################################################################
inputDirectory = "/home/sim8/test.data/"
outputDirectory = "/home/sim8/assemblyMagicResults/"

#Output directories for respective assembler
ODerrors = "/home/sim8/assemblyMagicResults/errors/"
ODfastqc = "/home/sim8/assemblyMagicResults/fastQCresults/"
ODprinseq = "home/sim8/assemblyMagicResults/prinseq/"
ODedena = "/home/sim8/assemblyMagicResults/edena/"

inputfileOne = ""
inputfileTwo = ""

paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]
preProcess(paths)

fileHashInputDirectory = ODprinseq
fileHash = {}

prinseqPaths = [os.path.join(fileHashInputDirectory,fn) for fn in next(os.walk(fileHashInputDirectory))[2]]

wranglePairedEnds(prinseqPaths)
print fileHash