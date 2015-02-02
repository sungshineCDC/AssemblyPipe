__author__ = 'sungshine'
#!/usr/bin/python3
#Run FastQC on raw reads

import os
import sys
import subprocess

inputDirectory = "/home/biol8803b/data"
paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

#Invokes fastqc on raw read files passing in the files in as an argument
def moduleFastQC(file):
    subprocess.call(['fastqc', file])

for file in paths:
    moduleFastQC(file)
