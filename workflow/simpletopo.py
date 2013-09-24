# Workflow that takes a fasta file and a topology list and predicts the best possible result using a sliding window method.

#Generic:
#./runSimpleTopo.sh 
#	NAME_OF_SCALE
#	FOLDER_FASTA
#	TOPO_FILE_AS_LIST
#	IDENTIFIER
#	START_NUMBER_OPTIMIZATION
#	END_NUMBER_OPTIMIZATION
#	STEP_NUMBER_OPTIMIZATION

#Example:
#./runSimpleTopo.sh wimley /afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.chrisp.1/scampi/input/dataset_for_pdb_scale/simpletopo/most_hydrophobic/fasta/high/ /afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.chrisp.1/scampi/input/dataset_for_pdb_scale/simpletopo/most_hydrophobic/topo/high_topo.list high_res_130923 -2 2 0.1

import sys
import os

def main(sScale, sFastaFolder, sTopoFile, sIdentifier, iStartNumberOpimization, iEndNumberOpimization, iStepNumberOpimization):
    os.system("../helper/simpletopo/runSimpleTopo.sh " + sScale + " " + sFastaFolder + " "  
                                                       + sTopoFile + sIdentifier + " " 
                                                       + iStartNumberOpimization + " " 
                                                       + iEndNumberOpimization + " " 
                                                       + iStepNumberOpimization)


if __name__ == '__main__':
    if len(sys.argv) == 8:
        sScale = sys.argv[1]
        sFastaFolder = sys.argv[2]
        sTopoFile = sys.argv[3]
        sIdentifier = sys.argv[4]
        iStartNumberOpimization = sys.argv[5]
        iEndNumberOpimization = sys.argv[6]
        iStepNumberOpimization = sys.argv[7]

        main(sScale, sFastaFolder, sTopoFile, sIdentifier, iStartNumberOpimization, iEndNumberOpimization, iStepNumberOpimization)

    else:
        print "../helper/simpletopo.py NAME_OF_SCALE FOLDER_FASTA TOPO_FILE_AS_LIST IDENTIFIER START_NUMBER_OPTIMIZATION END_NUMBER_OPTIMIZATION STEP_NUMBER_OPTIMIZATION"