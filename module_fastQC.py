__author__ = 'sungshine'
#!/usr/bin/python3
#Invokes fastqc on raw read files passing in the files in as an argument

import os
import sys
import subprocess

inputDirectory = sys.argv[1]    #/home/biol8803b/tmp
outputDirectory = sys.argv[2]   #/home/biol8803b/fastQCresults
paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

def moduleFastQC(file):
    subprocess.call(['fastqc', "-o", ODfastqc, file,])

# moduleFastQC(file, outputDirectory)
