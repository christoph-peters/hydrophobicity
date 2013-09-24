#!/bin/bash

if [ ${#1} -lt 1 ]; then
    /bin/echo "comparePredictions<PredictionDir> <StructureFile>"
    exit
fi

#args
predictiondir=$1
INPUTTOPOLIST=$2
SCALE=$3
IDENTIFY=$4
filenames=""

for dir in $predictiondir*
do
 WINDOWSIZE=$(basename $dir)
mkdir /afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.chrisp.1/scampi/output/simpletopo/$WINDOWSIZE/ 2>/dev/null
./comparePredictions.sh /scratch/chrisp/simpletopo/$SCALE/combined/$SCALE/$WINDOWSIZE/ $INPUTTOPOLIST > /afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.chrisp.1/scampi/output/simpletopo/$WINDOWSIZE'/'$IDENTIFY'_'$SCALE.res
done
