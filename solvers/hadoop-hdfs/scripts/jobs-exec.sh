#!/bin/bash

hadoop jar \
    /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
    -files scripts/stage1Mapper.py,scripts/stage1Reducer.py,data/ghcnd-states.txt,data/ghcnd-stations.txt \
    -input /workspace/data/2019.csv \
    -output /workspace/output/stage1 \
    -mapper stage1Mapper.py \
    -reducer stage1Reducer.py

hadoop jar \
    /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
    -files scripts/stage2Mapper.py,scripts/stage2Reducer.py \
    -input /workspace/output/stage1 \
    -output /workspace/output/stage2 \
    -mapper stage2Mapper.py \
    -reducer stage2Reducer.py

hadoop jar \
    /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
    -files scripts/stage3Mapper.py,scripts/stage3Reducer.py,data/ghcnd-states.txt \
    -input /workspace/output/stage2 \
    -output /workspace/output/stage3 \
    -mapper stage3Mapper.py \
    -reducer stage3Reducer.py

mkdir -p /hadoop/workspace/output
hdfs dfs -getmerge /workspace/output/stage3 /hadoop/workspace/output/report.csv
chown $PUID:$PGID -R /hadoop/workspace/output