#!/usr/bin/python

# new way to calculate sliding window results 

import sys,re, os;

sys.path.append("/".join(os.path.realpath(__file__).split("/")[0:-4]))

from lib import io
from lib import math_and_statistics

repeat = re.compile(r'((?P<start>[M])(?P=start)+[\.]*)|(?P<test>[M])')

def compareTop(strPredictionTemp, strStructureTemp) :
    strucList = []
    predList = []

    for match in repeat.finditer(strStructureTemp):
        strucList.append([match.start(),match.end()])

    for match in repeat.finditer(strPredictionTemp):
        predList.append([match.start(),match.end()])


    for x in range(0, len(strucList)):
        iStart = strucList[x][0]
        iEnd = strucList[x][1]
        bFoundCorrect = False

        for i in range(0, len(predList)):
            bFoundStart = False
            bFoundEnd = False

            if iStart + 5 >= predList[i][0] and iStart - 5  <= predList[i][0]:
                bFoundStart = True

            if bFoundStart is True:
                if iEnd + 5 >= predList[i][1] and iEnd - 5  <= predList[i][1]:
                    bFoundEnd = True

            if bFoundStart is True and bFoundEnd is True:
                bFoundCorrect = True
                break
    if bFoundCorrect is True:
        bFoundCorrect = False
        for x in range(0, len(predList)):
            iStart = predList[x][0]
            iEnd = predList[x][1]
            bFoundCorrect = False

            for i in range(0, len(strucList)):
                bFoundStart = False
                bFoundEnd = False

                if iStart + 5 >= strucList[i][0] and iStart - 5  <= strucList[i][0]:
                    bFoundStart = True

                if bFoundStart is True:
                    if iEnd + 5 >= strucList[i][1] and iEnd - 5  <= strucList[i][1]:
                        bFoundEnd = True

                if bFoundStart is True and bFoundEnd is True:
                    bFoundCorrect = True
                    break
        if bFoundCorrect is True:
            return 1
        else:
            return 0

    else:
        return 0
        

def comparePerAA(pred_seq, struc_seq):
    iTP = 0
    iFP = 0
    iTN = 0
    iFN = 0

    if len(pred_seq) == len(struc_seq):
        for i in range(0, len(pred_seq)):
            if pred_seq[i] == struc_seq[i] and struc_seq[i] == "M":
                iTP += 1
            elif pred_seq[i] == struc_seq[i]:
                iTN += 1
            elif struc_seq[i] == "M":
                iFN += 1
            elif struc_seq[i] != ".":
                iFP += 1

        return float(math_and_statistics.calc_MCC_single_values(iTP, iFN, iTN, iFP)[4])



if __name__ == '__main__' :
    filePrediction = io.readFile(sys.argv[1])[0]#"/Users/christoph/threshold-0.1")[0]#sys.argv[1])
    fileStructure  = io.readFile(sys.argv[2])[0]#"/afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.chrisp.1/scampi/input/Kostas_novel_dataset/kostas_topo.list")[0]#sys.argv[2])
    #print sys.argv[1]
    #print sys.argv[2]
    
    iAll = 0
    iCorrect = 0
    
    fileStructure = [entry.replace("i", "o") for entry in fileStructure]
    #print len(filePrediction)
    #print len(fileStructure)
    #exit()

    for i in range(0, len(filePrediction)):
        iCorrect += comparePerAA(filePrediction[i], fileStructure[i])
        iAll += 1

    print iCorrect/float(iAll)

