__author__ = 'sungshine'
#!/usr/bin/python
#Create directories taken from STDIN

import os
import sys

inputDirectory = sys.argv[1]
outputDirectory = sys.argv[2]

def makeOutDirectory(outputDirectory):

    if not os.path.exists(outputDirectory):
        os.makedirs(outputDirectory)

makeOutDirectory(outputDirectory)