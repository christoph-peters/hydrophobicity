#!/bin/bash

if [ ${#1} -lt 1 ]; then
    /bin/echo "comparePredictions<PredictionDir> <StructureFile>"
    exit
fi

#args
predictiondir=$1
structureFile=$2
filenames=""

for file in $predictiondir*
do
  echo $file
 ../helper/simpletopo/comparePredictionsNew.py ${file} $structureFile
done
