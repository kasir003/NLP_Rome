#!/bin/sh

# Variable to store input file
INPUTFILE='./Input/tell-verb-chime006-2.xml'

# Variable to store target word
TARGET_WORD1='tell'

# Variable to store target word 2, used only for name conflate
#TARGET_WORD2='heaven'

# Variable to store output file
OUTPUTFILE='./Output/tell-verb-chime006-out.xml' 

# Variable to store location of senseclusterscorer.sh
SENSE_CLUSTERS_SCORER_LOCATION='./senseclusters_scorer'

python3 main.py -i $INPUTFILE -o $OUTPUTFILE -k1 $TARGET_WORD1 

# Change this to other format for running name-conflate input file
#python3 main.py -n $INPUTFILE -o $OUTPUTFILE -k1 $TARGET_WORD1 -k2 $TARGET_WORD2

# sleep 5 seconds
sleep 5s
# move key files to sensecluster scorer location

mv inputkey.key $SENSE_CLUSTERS_SCORER_LOCATION
mv outputkey.key $SENSE_CLUSTERS_SCORER_LOCATION

# Change directory to senseclustersscorer.sh location
cd $SENSE_CLUSTERS_SCORER_LOCATION

# Run senseclusters_scorer.sh
./senseclusters_scorer.sh outputkey.key inputkey.key

# Print confusion matrix
cat report.out








