DIRECTORY=$1
SCALE=$2
for dir in $DIRECTORY/$SCALE/*; do
   for subdir in $dir/*; do
	for i in $(ls -1 $subdir ); do  	
	WINDOWSIZE=$(basename $dir)
	mkdir /scratch/chrisp/simpletopo/$SCALE/combined 2>/dev/null
	mkdir /scratch/chrisp/simpletopo/$SCALE/combined/$SCALE 2>/dev/null
	mkdir /scratch/chrisp/simpletopo/$SCALE/combined/$SCALE/$WINDOWSIZE 2>/dev/null
	THRESHOLD=$(basename $subdir)
cat -- $subdir/$i >> /scratch/chrisp/simpletopo/$SCALE/combined/$SCALE/$WINDOWSIZE/$THRESHOLD
     done
    done
  done
