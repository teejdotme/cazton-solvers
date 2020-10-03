#!/bin/bash

mkdir -p /hadoop/workspace/output
hdfs dfs -getmerge /workspace/output/report /hadoop/workspace/output/report.csv
sed -i '1 i\STATE,NAME,MIN TEMP,MAX TEMP,AVG TEMP,VARIANCE' /hadoop/workspace/output/report.csv
chown $PUID:$PGID -R /hadoop/workspace/output