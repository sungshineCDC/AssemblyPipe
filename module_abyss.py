import os
import sys
import subprocess
import re

inputDirectory = '/home/biol8803b/tmp/'
outputDirectory = '/home/biol8803b/assemblies/'

paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

def moduleAbyssSE(file):
	base = re.match("^(.*)_", file)
	filename = base.group(1)
	subprocess.call(["ABYSS.py", "-k 21", inputDirectory + file, "-o", outputDirectory + filename + ".fa"])

def moduleAbyssPE(inputfileone, inputfiletwo):
	base = re.match("^(.*)_", file)
	filename = base.group(1)
	subprocess.call(["abyss-pe"], "k=21", "name=", filename, "in=", inputDirectory + inputfileone, inputDirectory + inputfiletwo]
