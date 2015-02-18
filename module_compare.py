__author__ = 'mcdy143'
#!/usr/bin/python3
import os
import subprocess
import csv
from math import log

inputDirectory_edena = "/home/sim8/assemblyMagicResults/edena/"
inputDirectory_abyss = "/home/sim8/assemblyMagicResults/abyss/"
inputDirectory_spades = "/home/sim8/assemblyMagicResults/spades/"
folders_edena = [os.path.join(inputDirectory_edena,fn) for fn in next(os.walk(inputDirectory_edena))[1]]
folders_abyss = [os.path.join(inputDirectory_abyss,fn) for fn in next(os.walk(inputDirectory_abyss))[1]]
folders_spades = [os.path.join(inputDirectory_spades,fn) for fn in next(os.walk(inputDirectory_spades))[1]]

resultFile = "/home/ywang936/reads/preprocessed/edena_output/quast_results/latest/report.tsv"
def file2Dict(resultFile):
    with open(resultFile, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        dataList = list(reader)
    return {item[0]:item[1] for item in dataList}

def calcScore(resultDict):
    numContigs = float(resultDict['# contigs'])
    n50 = float(resultDict['N50'])
    genlen = float(resultDict['Total length'])
    score = log((n50 * genlen) / numContigs)
    return score

'''
for folder in folders_edena:
    filePath = folder + "/_contigs.fasta"
    subprocess.call(["/home/agupta399/installation/quast-2.3/quast.py", "-o", folder, filePath])
for folder in folders_spades:
    filePath = folder + "/scaffolds.fasta"
    subprocess.call(["/home/agupta399/installation/quast-2.3/quast.py", "-o", folder, filePath])
for folder in folders_abyss:
    filePath = folder + "/contigs.fasta"
    subprocess.call(["/home/agupta399/installation/quast-2.3/quast.py", "-o", folder, filePath])
'''
resultDict = file2Dict(resultFile)
print calcScore(resultDict)
