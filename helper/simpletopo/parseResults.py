#!/usr/bin/python

import os,subprocess,sys,time

def main():
	#resultdir = "/afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.chrisp.1/scampi/output/simpletopo/"
	resultdir = sys.argv[1]
	scaleNameString = ""
	windowDirs = os.listdir(resultdir)
	resultList = []
	for window in windowDirs:
		scaleNameString = ""
		windowName=window.replace("window_","")
		resultRow = str(windowName)
		resultFiles = os.listdir(resultdir + window + "/")
		resultFiles.sort()
		for resultFile in resultFiles:
			highestResult = 0
			scaleName = resultFile.split("_")[3].replace(".res","")
			scaleNameString = scaleNameString + ";" + scaleName
			fileResult = open(resultdir + window + "/" + resultFile,"r")
			for line in fileResult:
				if "/" not in line:
					resultValueTemp = line
					if float(resultValueTemp) > highestResult:
						highestResult = float(resultValueTemp)
			resultRow = resultRow + ";" + str(highestResult)
		resultList.append(resultRow)	
	outFile = open(resultdir.replace("simpletopo/","") + "completeOutput.txt","w")
	outFile.write(scaleNameString + "\n")
	for i in range(0,len(resultList)):
		outFile.write(resultList[i] + "\n")
	outFile.close()


if __name__=="__main__":
	main();
