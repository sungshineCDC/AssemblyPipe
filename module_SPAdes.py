__author__ = 'sungshine'
#!/usr/bin/python3

import os
import sys
import subprocess

inputDirectory = "/home/biol8803b/tmp"
outputDirectory = "/home/biol8803b/assemblies/"
paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

def moduleSpadesSE(file):
    base = os.path.basename(file)
    filename = os.path.splitext(base)[0]
    subprocess.call(["spades.py", "--careful", "-s", file, "-o", outputDirectory+filename+".spades",])

def moduleSpadesPE(inputfileone, inputfiletwo):
    subprocess.call(["spades.py", "--careful", "-1", inputfileone, "-2", inputfiletwo, "-o", outputDirectory+ ])

for file in paths:

    moduleSpadesSE(file)
