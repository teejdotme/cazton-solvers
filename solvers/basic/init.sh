rm -Rf ./input
rm -Rf ./output
mkdir -p ./input
mkdir -p ./output/intermediate

gzip -dc ../../data/2019.csv.gz > ./input/2019.csv
cp ../../data/ghcnd-states.txt ./input/
cp ../../data/ghcnd-stations.txt ./input/