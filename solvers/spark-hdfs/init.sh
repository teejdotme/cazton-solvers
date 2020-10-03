#!/bin/bash

mkdir -p ./workspace/data
mkdir -p ./workspace/scripts

gzip -dc ../../data/2019.csv.gz > ./workspace/data/2019.csv
cp ../../data/ghcnd-states.txt ./workspace/data/
cp ../../data/ghcnd-stations.txt ./workspace/data/

cp ./scripts/* ./workspace/scripts/

docker-compose -f ./docker/docker-compose.yml exec hdfs-workspace /bin/bash /hadoop/workspace/scripts/hdfs-load.sh