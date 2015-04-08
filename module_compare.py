__author__ = 'mcdy143'
#!/usr/bin/python3
import csv
from math import log, log10
from collections import defaultdict
import os

inputDirectory_edena = "/home/sim8/assemblyMagicResults/edena/"
inputDirectory_abyss = "/home/sim8/assemblyMagicResults/abyss/"
inputDirectory_spades = "/home/sim8/assemblyMagicResults/spades/"
inputDirectory_reference = "/home/sim8/assemblyMagicResults/reference/"
inputDirectory_cisa = "/home/sim8/assemblyMagicResults/CISA/"
folders_edena = [os.path.join(inputDirectory_edena,fn) for fn in next(os.walk(inputDirectory_edena))[1]]
folders_abyss = [os.path.join(inputDirectory_abyss,fn) for fn in next(os.walk(inputDirectory_abyss))[1]]
folders_spades = [os.path.join(inputDirectory_spades,fn) for fn in next(os.walk(inputDirectory_spades))[1]]
folders_reference = [os.path.join(inputDirectory_reference,fn) for fn in next(os.walk(inputDirectory_reference))[1]]
folders_cisa = [os.path.join(inputDirectory_cisa,fn) for fn in next(os.walk(inputDirectory_cisa))[1]]

# takes in a report.tsv file and returns a dictionary containing all attributes as keys
# and their respective values
def file2Dict(resultFile):
    with open(resultFile, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        dataList = list(reader)
    # check GC content to decide on expected length
    # option1: use average as expeceted Length
    # expectedLength = (2200000 + 1900000) / 2
    # option2: use GC content
    GCcontent = float(dataList[8][1])
    expectedLength = 0
    if GCcontent >= 49.5 and GCcontent <= 52.5:
        expectedLength = 2200000
    elif GCcontent >= 36.5 and GCcontent <= 39.5:
        expectedLength = 1900000
    else:
        expectedLength = 0
    return {item[0]:item[1] for item in dataList}, expectedLength

# takes in a dictionary and outputs the score calculated
def calcScore(resultDict, expectedLen):
    if expectedLen == 0:
        return 0
    genlen = float(resultDict['Total length'])
    genomeComp = genlen / expectedLen
    numContigs = float(resultDict['# contigs'])
    n50 = float(resultDict['N50'])
    score = log10(n50 / numContigs) * (genomeComp**2)
    return score

# takes in a list of directory (for a certain assembler) and assembler name, calculates score
# for each report file under each directory, and store results in a 2-d dictionary: 
# {M10699:{edenascore: ###, spadesscore: ###, abyssscore: ###, cisa score: ###}, M10562:...}
scoreDict = defaultdict(dict)
def makeScoreDict(directory, assembler):
    for f in next(os.walk(directory))[1]:
        try:
            filePath = os.path.join(directory,f) + "/report.tsv"
            fileKey = f[:6]
            resultDict, expectedLen = file2Dict(filePath)
            score = calcScore(resultDict, expectedLen)
            scoreDict[fileKey][assembler] = score
        except:
            pass
    return scoreDict

def scoreDict2File(scoreDict):
    outFile = open("scores_gc.csv", 'w')
    outFile.write("Read\tabyss\tspades\tedena\treference\tCISA\n")
    # add cisa later
    assemblers = ['abyss', 'spades', 'edena', 'reference', 'cisa']
    for assembly in scoreDict:
        outFile.write(assembly+"\t")
        for assembler in assemblers:
            try:
                outFile.write(str(scoreDict[assembly][assembler])+"\t")
            except:
                outFile.write("Missing"+"\t")
        outFile.write("\n")

# =======Example Usage========= #
'''
resultFile = "/home/sim8/assemblyMagicResults/spades/M25823_S3_L001_R1_001.prinseq.spades/report.tsv"
resultDict, eLength = file2Dict(resultFile)
print calcScore(resultDict, eLength)
'''
scoreDict = makeScoreDict(inputDirectory_abyss, 'abyss')
scoreDict = makeScoreDict(inputDirectory_spades, 'spades')
scoreDict = makeScoreDict(inputDirectory_edena, 'edena')
scoreDict = makeScoreDict(inputDirectory_reference, 'reference')
scoreDict = makeScoreDict(inputDirectory_cisa, 'cisa')
'''
print len(scoreDict.keys())
for f in scoreDict:
    print "file: " + f
    print len(scoreDict[f].keys()) == 4
    for assembler in scoreDict[f]:
        print "assembler: " + assembler + "; score: " + str(scoreDict[f][assembler])
'''

scoreDict2File(scoreDict)

# ============================= #
