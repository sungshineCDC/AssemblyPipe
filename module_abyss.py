import os
import sys
import subprocess
import re

inputDirectory = '/home/sim8/assemblyMagicResults/prinseq/'
ODabyss = '/home/sim8/assmeblyMagicResults/abyss/'

paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

def moduleAbyssSE(inputfileOne):
	base = re.match("^(.*)_", inputfileOne)
	filename = base.group(1)
	subprocess.call(["ABYSS", "-k 21", inputDirectory + file, "-o", ODabyss + filename + ".fa"])

def moduleAbyssPE(inputfileOne, inputfileTwo):
	base = re.match("^(.*)_", file)
	filename = base.group(1)
	os.system("cd "+ODabyss)
	subprocess.call(["abyss-pe"], "k=21", "name=", ODabyss + filename + ".fa", "in=", inputDirectory + inputfileOne, inputDirectory + inputfileTwo]
