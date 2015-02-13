__author__ = 'sungshine'
#!/usr/bin/python3
#assemblyMagic Pipeline

import os
import sys
import subprocess
import re

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

#Invokes SPAdes on single-end reads or paired-end reads
def moduleSpadesSE(inputfileOne):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    subprocess.call(["spades.py", "--careful", "-s", inputfileOne, "-o", outputDirectory+filename+".spades",])

def moduleSpadesPE(inputfileOne, inputfileTwo):
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    subprocess.call(["spades.py", "--careful", "-1", inputfileOne, "-2", inputfileTwo, "-o", outputDirectory+filename".spades",])

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

inputDirectory = '' #/home/biol8803b/data
outputDirectory = ''   #/home/biol8803b/assemblyMagicResults/preProcessed

#parse command line options
try:
    opts, args = getopt.getopt(argv, "hi:o:")
except getopt.GetoptError:
    print 'usage: ./assemblyMagic.py -i <Raw reads Directory> -o <output Directory>\n'
    sys.exit()
for opt, arg in opts:
    if opt == '-h':
        print 'usage: ./assemblyMagic.py -i <Raw reads Directory> -o <output Directory>\n'
        sys.exit()
    elif opt in ('-i'):
        inputDirectory = arg
    elif opt in ('-o'):
        outputDirectory = arg

#Output directories for respective assembler
ODspades = "/home/sim8/assemblyMagicResults/spades/"
ODabyss = "/home/sim8/assemblyMagicResults/abyss/"
ODedena = "/home/sim8/assemblyMagicResults/edena/"
ODcisa = "/home/sim8/assemblyMagicResults/cisa/"
inputfileOne = ""
inputfileTwo = ""
paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]
prinseqPaths = [os.path.join(outputDirectory,fn) for fn in next(os.walk(outputDirectory))[2]]

fileHash = {}
assemblyHash ={}

makeOutDirectory(outputDirectory)
preProcess(paths)
wranglePairedEnds(prinseqPaths)

for key in fileHash:

    currentValue = fileHash.get(key)
    
    #call assemblers to execute single-end read
    if len(currentValue) == 1:
        inputfileOne = currentValue[0]
        
        moduleSpadesSE(inputfileOne)
        moduleAbyssSE(inputfileone)
    
    #execute paired-end reads
    if len(currentValue) == 2:
        inputfileOne = currentValue[0]
        inputfileTwo = currentValue[1]
        
        moduleSpadesPE(inputfileOne, inputfileTwo)
        moduleAbyssPE(inputfileOne, inputfileTwo)
