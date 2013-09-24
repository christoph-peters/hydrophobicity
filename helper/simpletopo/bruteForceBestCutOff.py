#!/usr/bin/python

import sys, os
from optparse import OptionParser 
parser = OptionParser()

def main():
    sScale = sys.argv[1]
    temp = sys.argv[2] 
    print (temp)
    iLowerRange = temp
    iLowerRange = float(iLowerRange) * 1000
    temp = sys.argv[3]
    iHigherRange = temp
    iHigherRange = float(iHigherRange) * 1000
    temp = sys.argv[4]
    dStepSize = temp
    dStepSize = float(dStepSize) * 1000
    sInput = "/scratch/chrisp/simpletopo/" + sScale + "/firststep/"
    
    filenameList = os.listdir(sInput + sScale + "/")
    for i in range(int(iLowerRange), int(iHigherRange), int(dStepSize)):
        iThreshold = float(float(i)/float(1000))
        for file in filenameList:
            outFile = file.split(".")[0]
            iWindowsize = file.split("_")[0]
            sTopoSeq = ""
            if file.find("._") != 0:
                fileFasta = open(sInput + sScale + "/" + file, 'r')
                for line in fileFasta:
                    fValue = line.replace("\n","")
                    if float(fValue) < iThreshold:
                        sTopoSeq += "M"
                    else:
                        sTopoSeq += "o"
                if not os.path.exists("/scratch/chrisp/simpletopo/" + sScale + "/secondstep/"):
                    os.makedirs("/scratch/chrisp/simpletopo/" + sScale + "/secondstep/")
                if not os.path.exists("/scratch/chrisp/simpletopo/" + sScale + "/secondstep/" + sScale):
                    os.makedirs("/scratch/chrisp/simpletopo/" + sScale + "/secondstep/" + sScale)
                if not os.path.exists("/scratch/chrisp/simpletopo/" + sScale + "/secondstep/" + sScale + "/window_" + str(iWindowsize) + "/"):
                    os.makedirs("/scratch/chrisp/simpletopo/" + sScale + "/secondstep/" + sScale + "/window_" + str(iWindowsize) + "/")
                if not os.path.exists("/scratch/chrisp/simpletopo/" + sScale + "/secondstep/" + sScale + "/window_" + str(iWindowsize) + "/threshold" + str(iThreshold)):
                    os.makedirs("/scratch/chrisp/simpletopo/" + sScale + "/secondstep/" + sScale + "/window_" + str(iWindowsize) + "/threshold" + str(iThreshold))
                fileWrite = open("/scratch/chrisp/simpletopo/" + sScale + "/secondstep/" + sScale + "/window_" + str(iWindowsize) + "/threshold" + str(iThreshold) + "/" + outFile  + ".top", 'w')
                fileWrite.write(">" + outFile + "\n" + sTopoSeq + "\n")
                fileWrite.close()

if __name__=="__main__":
    main();
