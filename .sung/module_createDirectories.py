__author__ = 'sungshine'
#!/usr/bin/env python
import os
import sys
import subprocess

outputDirectory = sys.argv[1]

def module_createDirectories(outputDirectory):

    ODerrors = outputDirectory+"errors/"
    ODfastqc = outputDirectory+"fastqc/"
    ODfastqcpost = outputDirectory+"fastqcpost/"
    ODprinseq = outputDirectory+"prinseq/"
    ODspades = outputDirectory+"spades/"
    ODedena = outputDirectory+"edena/"
    ODabyss = outputDirectory+"abyss/"

    OD = [ODerrors, ODfastqc, ODfastqcpost, ODprinseq, ODspades, ODedena, ODabyss,]

    os.mkdir(outputDirectory)
    os.chdir(outputDirectory)

    for





















# inputDirectory = "/home/sim8/test.data/"
# ODabyss = "/home/sim8/my.abyss/"
# paths = [os.path.join(inputDirectory,fn) for fn in next(os.walk(inputDirectory))[2]]
#
# def module_createDirectories(file):
#     base = os.path.basename(file)
#     filename = os.path.splitext(base)[0]
#     fileOutputDirectory = ODabyss+str(filename)+".abyss"
#
#     if not os.path.exists(fileOutputDirectory):
#         print "Creating directory: "+fileOutputDirectory
#         os.makedirs(fileOutputDirectory)
#         os.chdir(fileOutputDirectory)
#         print "Pretending to cal Abyss on "+filename
#     subprocess.call(["touch", filename+"testfile",])
#
# for file in paths:
#     module_createDirectories(file)