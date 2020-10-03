#!/bin/bash

mkdir -p /hadoop/workspace/output
hdfs dfs -getmerge /workspace/output/report /hadoop/workspace/output/report.csv
chown $PUID:$PGID -R /hadoop/workspace/output