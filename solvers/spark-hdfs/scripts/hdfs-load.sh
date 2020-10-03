#!/bin/bash

hdfs dfs -mkdir -p /workspace
hdfs dfs -put /hadoop/workspace/data /workspace/
hdfs dfs -put /hadoop/workspace/scripts /workspace/