SCALE=$1
INPUTFASTA=$2
INPUTTOPOLIST=$3
IDENTIFY=$4
LOWERRANGE=$5
HIGHERRANGE=$6
STEPSIZE=$7
#sleep $(($RANDOM % 100))
mkdir /scratch/chrisp/simpletopo 2>/dev/null
mkdir /scratch/chrisp/simpletopo/$SCALE 2>/dev/null
./simpleTopologyPredictionForBruteForce.py $SCALE $INPUTFASTA
./bruteForceBestCutOff.py $SCALE $LOWERRANGE $HIGHERRANGE $STEPSIZE
./createFilesForComparison.sh /scratch/chrisp/simpletopo/$SCALE/secondstep/ $SCALE
./comparePredictionsWindow.sh /scratch/chrisp/simpletopo/$SCALE/combined/$SCALE/ $INPUTTOPOLIST $SCALE $IDENTIFY
rm -rf /scratch/chrisp/simpletopo/$SCALE
python parseResults.py /afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.chrisp.1/scampi/output/simpletopo/
python plot_sliding_window.py