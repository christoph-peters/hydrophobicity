#!/usr/bin/python

import sys, os

namesHydro = {"opm1":0,"opm2":1,"opm3":2,"hopp":3,"ges":4,"wimley":5,"hessa":6,"eisenberg":7,"kyte":8,"guy":9,"janin":10,"uhs":11,"moon":12,"pm1d":13,"pm3d":14}
dirHydro = [{"A":-0.22, "C":-0.16, "D":1.17,"E":1.23,"F":-0.50,"G":-0.09,"H":0.52,"I":-0.46,"K":1.17,"L":-0.38,"M":-0.24,
                "N":0.60,"P":0.34,"Q":0.62,"R":1.05,"S":0.20,"T":0.05,"V":-0.35,"W":-0.17,"Y":-0.01}, #OPM1             
            {"A":-0.23, "C":-0.20, "D":1.19,"E":1.17,"F":-0.39,"G":-0.12,"H":0.59,"I":-0.41,"K":1.37,"L":-0.32,"M":-0.15,
                "N":0.56,"P":0.33,"Q":0.59,"R":1.28,"S":0.19,"T":0.01,"V":-0.32,"W":0.10,"Y":0.18}, #OPM2   
            {"A":-0.22, "C":-0.26, "D":1.26,"E":1.22,"F":-0.52,"G":-0.06,"H":0.64,"I":-0.55,"K":1.39,"L":-0.42,"M":-0.22,
                "N":0.74,"P":0.45,"Q":0.81,"R":1.29,"S":0.22,"T":0.12,"V":-0.42,"W":0.03,"Y":0.17}, #OPM3
            #{"A":-0.20, "C":-0.30, "D":1.85,"E":2.26,"F":-0.48,"G":0.06,"H":1.68,"I":-0.62,"K":3.03,"L":-0.50,"M":-0.13,
            #    "N":1.46,"P":0.74,"Q":1.18,"R":2.11,"S":0.38,"T":0.28,"V":-0.48,"W":0.36,"Y":0.59}, #OPM3
            {"A":-0.5, "C":-1, "D":3,"E":3,"F":-2.5,"G":0,"H":-0.5,"I":-1.8,"K":3,"L":-1.8,"M":-1.3,
                "N":0.2,"P":0,"Q":0.2,"R":3,"S":0.3,"T":-0.4,"V":-1.5,"W":-3.4,"Y":-2.3}, #Hopp
            {"A":-1.6, "C":-2, "D":9.2,"E":8.2,"F":-3.7,"G":-1,"H":3,"I":-3.1,"K":8.8,"L":-2.8,"M":-3.4,
                "N":4.8,"P":0.2,"Q":4.1,"R":12.3,"S":-0.6,"T":-1.2,"V":-2.6,"W":-1.9,"Y":0.7}, #ges
            {"A":0.5, "C":-0.02, "D":3.64,"E":3.63,"F":-1.71,"G":1.15,"H":2.33,"I":-1.12,"K":2.80,"L":-1.25,"M":-0.67,
                "N":0.85,"P":0.14,"Q":0.77,"R":1.81,"S":0.46,"T":0.25,"V":-0.46,"W":-2.09,"Y":-0.71}, #Wimley
            {"A":0.11, "C":-0.13, "D":3.49,"E":2.68,"F":-0.32,"G":0.74,"H":2.06,"I":-0.6,"K":2.71,"L":-0.55,"M":-0.1,
                "N":2.05,"P":2.23,"Q":2.36,"R":2.58,"S":0.84,"T":0.52,"V":-0.31,"W":0.3,"Y":0.68}, #Hessa
            {"A":-0.62, "C":-0.29, "D":0.9,"E":0.74,"F":-1.19,"G":-0.48,"H":0.4,"I":-1.38,"K":1.5,"L":-1.06,"M":-0.64,
                "N":0.78,"P":-0.12,"Q":0.85,"R":2.53,"S":0.18,"T":0.05,"V":-1.08,"W":-0.81,"Y":-0.26}, #Eisenberg
            {"A":-1.8, "C":-2.5, "D":3.5,"E":3.5,"F":-2.8,"G":0.4,"H":3.2,"I":-4.5,"K":3.9,"L":-3.8,"M":-1.9,
                "N":3.5,"P":1.6,"Q":3.5,"R":4.5,"S":0.8,"T":0.7,"V":-4.2,"W":0.9,"Y":1.3}, #kyte
            {"A":0.1, "C":-1.42, "D":0.78,"E":0.83,"F":-2.12,"G":0.33,"H":-0.5,"I":-1.13,"K":1.4,"L":-1.18,"M":-1.59,
                "N":0.48,"P":0.73,"Q":0.95,"R":1.91,"S":0.52,"T":0.07,"V":-1.27,"W":-0.51,"Y":-0.21}, #guy
            {"A":-0.3, "C":-0.9, "D":0.6,"E":0.7,"F":-0.5,"G":-0.3,"H":0.1,"I":-0.7,"K":1.8,"L":-0.5,"M":-0.4,
                "N":0.5,"P":0.3,"Q":0.7,"R":1.4,"S":0.1,"T":0.2,"V":-0.6,"W":-0.3,"Y":0.4}, #janin
            {"A":-0.16, "C":0.01, "D":0.73,"E":0.7,"F":-0.46,"G":-0.2,"H":0.38,"I":-0.39,"K":0.9,"L":-0.3,"M":-0.2,
                "N":0.5,"P":0.5,"Q":0.46,"R":0.55,"S":0.06,"T":-0.01,"V":-0.25,"W":-0.03,"Y":-0.12},#uhs
            {"A":0, "C":0.49, "D":2.95,"E":1.64,"F":-2.2,"G":1.72,"H":4.76,"I":-1.56,"K":5.39,"L":-1.81,"M":-0.76,
                "N":3.47,"P":-1.52,"Q":3.01,"R":3.71,"S":1.83,"T":1.78,"V":-0.78,"W":-0.38,"Y":-1.09},#moon
            {"A":-0.17, "C":-0.06, "D":0.37,"E":0.15,"F":-0.41,"G":0.01,"H":-0.02,"I":-0.28,"K":0.32,"L":-0.28,"M":-0.26,
                "N":0.18,"P":0.13,"Q":0.26,"R":0.37,"S":0.05,"T":0.02,"V":-0.17,"W":-0.15,"Y":-0.09},#PM1D
            {"A":-0.15, "C":-0.15, "D":0.41,"E":0.30,"F":-0.22,"G":0.08,"H":0.06,"I":-0.29,"K":0.24,"L":-0.36,"M":-0.19,
                "N":0.22,"P":0.15,"Q":0.03,"R":0.32,"S":0.16,"T":-0.08,"V":-0.24,"W":-0.28,"Y":-0.03}]#PM3D

def calculateHydrophobicity(adWindow, weightedMatrix):
    hydroValue = 0
    weightedValue = 0
    for i in range(0,len(adWindow)):
        hydroValue = hydroValue + adWindow[i] * weightedMatrix[i]
        if adWindow[i] != 0:
            weightedValue += weightedMatrix[i]
    if weightedValue == 0:
        return 0;
    else:
        return (hydroValue/weightedValue) 
    
def fillMatrix(iWindowSize):
    lst = []
    for i in range(0, iWindowSize):
        if i < (iWindowSize/3):
            lst.append(1)
        elif i > (iWindowSize/3*2):
            lst.append(1)
        else:
            lst.append(2)
    return lst

def fillWindow(iWindowSize):
    lst = []
    for i in range(0, iWindowSize):
            lst.append(0)
    return lst

def main():
    sScale = sys.argv[1]
    sInput = sys.argv[2]
    iWindowsize = 15    
    sPathFasta = sInput
    if not os.path.exists("/scratch/chrisp/simpletopo/"):
        os.makedirs("/scratch/chrisp/simpletopo/")
    sOutput = "/scratch/chrisp/simpletopo/" + sScale
    if not os.path.exists(sOutput):
        os.makedirs(sOutput)
    sOutput = "/scratch/chrisp/simpletopo/" + sScale + "/firststep/"
    if not os.path.exists(sOutput):
        os.makedirs(sOutput)
    filenameList = os.listdir(sPathFasta)
    for iWindowsize in range(1,31,2):
        weightedMatrix = fillMatrix(iWindowsize)
        for filename in filenameList:
            if filename.find("._") != 0:
                adWindow = fillWindow(iWindowsize)
                hydroValuesList = []
                sSeqFastaTemp = ""
                fileFasta = open(sPathFasta + filename, 'r')
          
                for line in fileFasta:
                    if ">" not in line:
                        sSeqFastaTemp = sSeqFastaTemp + line.replace("\n","")
                sSeqFastaTemp.replace("X", "G")
                fileFasta.close()
                iRealWindowSize =10 
                iPos = 0
                for i in range(0,int(len(sSeqFastaTemp)+((iWindowsize-1)/2))):
                    if i < ((iWindowsize-1)/2):
                        #dCurrentWindow += dirHydro[sSeqFastaTemp[i]]
                        adWindow[int(((iWindowsize-1)/2)+i)] = dirHydro[namesHydro[sScale]][sSeqFastaTemp[i]]
                        #print (adWindow)
                    elif i < (iWindowsize-1):
                        #dCurrentWindow += dirHydro[sSeqFastaTemp[i]]
                        adWindow[iWindowsize-1] = dirHydro[namesHydro[sScale]][sSeqFastaTemp[i]]
                        #print (adWindow)
                        hydroValuesList.append(calculateHydrophobicity(adWindow, weightedMatrix))
                        del adWindow[0]
                        adWindow.append(0)
                        iPos += 1
                        iRealWindowSize += 1
                    elif i > (len(sSeqFastaTemp)-1):                  
                        del adWindow[0]
                        #print (adWindow)
                        hydroValuesList.append(calculateHydrophobicity(adWindow, weightedMatrix))
                        iPos += 1            
                    else:
			#print "--"
			#print sSeqFastaTemp
			#print sSeqFastaTemp[i]
			#print dirHydro[namesHydro[sScale]]
			#print sScale
			#print dirHydro[namesHydro[sScale]][sSeqFastaTemp[i]]	
			adWindow[iWindowsize-1] = dirHydro[namesHydro[sScale]][sSeqFastaTemp[i]]
                        #print (adWindow)
                        hydroValuesList.append(calculateHydrophobicity(adWindow, weightedMatrix))
			if (i+1) != (len(sSeqFastaTemp)):
                            del adWindow[0]
                            adWindow.append(0)
                        iPos += 1
                if not os.path.exists(sOutput + sScale):
                    os.makedirs(sOutput + sScale)
                fileWrite = open(sOutput + sScale + "/" + str(iWindowsize) + "_windowsize_"  + filename + ".hyd", 'w')
                for i in range(len(hydroValuesList)):
                    fileWrite.write(str(round(hydroValuesList[i],3)) + "\n")
                fileWrite.close()     
            

if __name__=="__main__":
    main();
