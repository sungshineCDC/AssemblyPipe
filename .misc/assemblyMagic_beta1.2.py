__author__ = 'mcdy143, sungshine, xin-w, anujg1911'
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

def moduleSpadesSE(inputfileOne):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    subprocess.call(["spades.py", "--careful", "-s", inputfileOne, "-o", ODspades+filename+".spades",])

def moduleSpadesPE(inputfileOne, inputfileTwo):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    subprocess.call(["spades.py", "--careful", "-1", inputfileOne, "-2", inputfileTwo, "-o", ODspades+filename+".spades",])

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

inputDirectory = "/home/sim8/assemblyMagicResults/prinseq"
outputDirectory = "/home/sim8/assemblyMagicResults/"

ODerrors = "/home/sim8/assemblyMagicResults/errors/"
ODprinseq = "/home/sim8/assemblyMagicResults/prinseq/"
ODfastqc = "/home/sim8/assemblyMagicResults/fastQCresults/"
ODedena = "/home/sim8/assemblyMagicResults/edena/"
ODspades = "/home/sim8/assemblyMagicResults/spades/"

fileHash = {}

# paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

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

        moduleSpadesSE(inputfileOne)
        moduleedenaSE(inputfileOne)

    if len(sortedValues) == 2:
        inputfileOne = sortedValues[0]
        inputfileTwo = sortedValues[1]

        moduleSpadesPE(inputfileOne, inputfileTwo)
        moduleedenaPE(inputfileOne, inputfileTwo)

#Code works here