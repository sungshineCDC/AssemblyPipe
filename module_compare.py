__author__ = 'mcdy143'
#!/usr/bin/python3
import csv
from math import log

# takes in a report.tsv file and returns a dictionary containing all attributes as keys
# and their respective values
def file2Dict(resultFile):
    with open(resultFile, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        dataList = list(reader)
    return {item[0]:item[1] for item in dataList}

# takes in a dictionary and outputs the score calculated
def calcScore(resultDict):
    numContigs = float(resultDict['# contigs'])
    n50 = float(resultDict['N50'])
    genlen = float(resultDict['Total length'])
    score = log((n50 * genlen) / numContigs)
    return score

# =======Example Usage========= #
resultFile = "/home/ywang936/reads/preprocessed/edena_output/quast_results/latest/report.tsv"

resultDict = file2Dict(resultFile)
print calcScore(resultDict)
