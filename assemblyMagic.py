__author__ = 'sungshine'
#!/usr/bin/python3
#assemblyMagic Pipeline

import os
import subprocess
import re
# import getopt, sys

#Takes STDIN for variables inputDirectory & outputDirectory, and creates the outputDirectory.
def makeOutDirectory(outputDirectory):
    if not os.path.exists(outputDirectory):
        os.makedirs(outputDirectory)

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

#Invokes fastqc on raw read files passing in the files in as an argument.
def moduleFastQC(file):
    subprocess.call(['fastqc', "-o", ODfastqc, file,])

#Invokes prinseq-lite on raw read files using default settings passing files in as argument.
def modulePrinseq(file):
    base = os.path.basename(file)
    filename = os.path.splitext(base)[0]
    subprocess.call(['prinseq-lite', '-verbose', '-fastq', file, '-out_format','3', '-out_good', ODprinseq+filename+".prinseq", "-out_bad", ODerrors+filename+".bad.prinseq",])

#Preprocess module, sets up directories and
def preProcess(paths):
    for file in paths:
        moduleFastQC(file)
        modulePrinseq(file)

#Invokes SPAdes on single-end reads or paired-end reads
def moduleSpadesSE(inputfileOne):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    subprocess.call(["spades.py", "--careful", "-s", inputfileOne, "-o", ODspades+filename+".spades",])

def moduleSpadesPE(inputfileOne, inputfileTwo):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    subprocess.call(["spades.py", "--careful", "-1", inputfileOne, "-2", inputfileTwo, "-o", ODspades+filename+".spades",])

#abyss single-end read function
def moduleAbyssSE(inputfileOne):
	base = re.match("^(.*)_", inputfileOne)
	filename = base.group(1)
	subprocess.call(["ABYSS", "-k 21", inputDirectory + file, "-o", ODabyss + filename + ".fa"])

#abyss paired-end read function (not sure if output directory is working atm)
def moduleAbyssPE(inputfileOne, inputfileTwo):
	base = re.match("^(.*)_", inputfileOne)
	filename = base.group(1)
	subprocess.call(["abyss-pe"], "k=21", "name=", ODabyss + filename + ".fa", "in=", inputDirectory + inputfileone, inputDirectory + inputfiletwo]


########################################################################################################################
###                                                   MAIN PROGRAM                                                   ###
########################################################################################################################

#parse command line options
# try:
#     opts, args = getopt.getopt(argv, "hi:o:")
# except getopt.GetoptError():
#     print 'usage: ./assemblyMagic.py -i <Raw reads Directory> -o <output Directory>\n'
#     sys.exit()
# for opt, arg in opts:
#     if opt == '-h':
#         print 'usage: ./assemblyMagic.py -i <Raw reads Directory> -o <output Directory>\n'
#         sys.exit()
#     elif opt in ('-i'):
#         inputDirectory = arg
#     elif opt in ('-o'):
#         outputDirectory = arg

inputDirectory = "/data/reads/"
outputDirectory = "/home/sim8/assemblyMagicResults/"

#Output directories for respective assembler
ODerrors = "/home/sim8/assemblyMagicResults/errors/"
ODprinseq = "home/sim8/assemblyMagicResults/prinseq/"
ODfastqc = "/home/sim8/assemblyMagicResults/fastqc/"
ODspades = "/home/sim8/assemblyMagicResults/spades/"
ODabyss = "/home/sim8/assemblyMagicResults/abyss/"
ODedena = "/home/sim8/assemblyMagicResults/edena/"
ODcisa = "/home/sim8/assemblyMagicResults/cisa/"

inputfileOne = ""
inputfileTwo = ""

paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]
preProcess(paths)

fileHashInputDirectory = str(ODprinseq)
fileHash = {}

prinseqPaths = [os.path.join(fileHashInputDirectory,fn) for fn in next(os.walk(fileHashInputDirectory))[2]]

wranglePairedEnds(prinseqPaths)
print fileHash

for key in fileHash:

    currentValue = fileHash.get(key)
    sortedValue = sorted(currentValue)

    #call assemblers to execute single-end read
    if len(sortedValue) == 1:
        inputfileOne = sortedValue[0]
        
        moduleSpadesSE(inputfileOne)
        moduleAbyssSE(inputfileOne)
    
    #execute paired-end reads
    if len(sortedValue) == 2:
        inputfileOne = sortedValue[0]
        inputfileTwo = sortedValue[1]
        
        moduleSpadesPE(inputfileOne, inputfileTwo)
        moduleAbyssPE(inputfileOne, inputfileTwo)
