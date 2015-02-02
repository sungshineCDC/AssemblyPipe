__author__ = 'sungshine'
#!/usr/bin/python3

import os
import sys
import subprocess

inputDirectory = "/Users/sungshine/Downloads/"
paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]

def wranglePairedEnds(paths):

    inputfileone = ""
    inputfiletwo = ""

    for file in paths:

        if "R1" in file:

            inputfileone = file
            queryname = file.replace("R1", "R2")
            print "Inputfileone is set as: "+inputfileone

            if os.path.exists(queryname):

                inputfiletwo = queryname
                print "Inputfiletwo is set as: "+inputfiletwo

            else:

                print os.path.basename(file)+" is a single end read"

wranglePairedEnds(paths)
