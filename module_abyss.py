import os
import sys
import subprocess
import re

inputDirectory = '/home/sim8/assemblyMagicResults/prinseq/'
outputDirectory = '/home/sim8/assmeblyMagicResults/abyss/'

paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

def moduleAbyssSE(file):
	base = re.match("^(.*)_", file)
	filename = base.group(1)
	subprocess.call(["ABYSS.py", "-k 21", inputDirectory + file, "-o", ODabyss + filename + ".fa"])

def moduleAbyssPE(inputfileone, inputfiletwo):
	base = re.match("^(.*)_", file)
	filename = base.group(1)
	subprocess.call(["abyss-pe"], "k=21", "name=", filename, "in=", inputDirectory + inputfileone, inputDirectory + inputfiletwo]