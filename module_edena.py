__author__ = 'mcdy143'
#!/usr/bin/env python
import os
import subprocess

#Calls program Edena in both overlap mode and assembly mode.
#Input file(s) are set to global variables: inputfileOne & inputfileTwo from fileHash{}.

def moduleedenaSE(inputfileOne):                #for single-end reads
    base = os.path.basename(inputfileOne)       #returns the file name without the path
    filename = os.path.splitext(base)[0]        #returns the file name without the file extension
    fileOutputDirectory = ODedena+str(filename)
    subprocess.call(["mkdir", fileOutputDirectory])
    subprocess.call(["edena", "-r", inputfileOne, "-p", fileOutputDirectory+"/out"])
    subprocess.call(["edena", "-e", fileOutputDirectory+"/out.ovl", "-p", fileOutputDirectory+"/"])

def moduleedenaPE(inputfileOne, inputfileTwo):      #for paired-end reads
    base = os.path.basename(inputfileOne)
    filename = os.path.splitext(base)[0]
    fileOutputDirectory = ODedena+str(filename)
    subprocess.call(["mkdir", fileOutputDirectory])
    subprocess.call(["edena", "-DRpairs", inputfileOne, inputfileTwo, "-p", fileOutputDirectory+"/out"])
    subprocess.call(["edena", "-e", fileOutputDirectory+"/out.ovl", "-p", fileOutputDirectory+"/"])