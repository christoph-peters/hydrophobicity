import os
import sys

scales = ["eisenberg", "ges", "guy", "hessa", "hopp", "janin", "kyte", "moon", "pm1d", "pm3d", "uhs", "wimley", "wimleyint"]
outPath = "/afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.chrisp.5/scampi_simpleTopo/"


for dataset in ["high"]: #, "low"]:
	
	topoPath = "/afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.chrisp.1/scampi/input/dataset_for_pdb_scale/simpletopo/most_hydrophobic/topo/" + dataset + "/"

	for scale in scales:
		outFile = outPath + dataset + "_" + scale + ".txt"
		pathIn = "/scratch/chrisp/simpletopo_" + dataset + "/" + scale + "/combined/" + scale + "/window_21/"

		with open(outFile, "w") as outFile:
			for threshold in os.listdir(pathIn):
				iTP = 0
				iTN = 0
				iFN = 0
				iFP = 0

				sfThres = threshold.replace("threshold","")

				fileIn = open(pathIn + threshold)
				for line in fileIn:
					if line.find(">") != -1:
						header = line.split("_")[2]
					else:
						predSeq = line.strip()

						fileTopo = open(topoPath + header.Upper() + ".top")

						for i in range(0, len(predSeq)):
							if topoSeq[i] == predSeq[i]:
								if topoSeq[i] == "M":
									iTP += 1
								else:
									iTN += 1
							else:
								if topoSeq[i] == "M":
									iFN += 1
								else:
									iFP += 1
				outFile.write([sfThres, str(iTP), str(iTN), str(iFN), str(iFP))




