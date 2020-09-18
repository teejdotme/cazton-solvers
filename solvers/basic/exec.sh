#!/bin/bash

rm -Rf ./output/*
mkdir -p ./output/intermediate
cat ./input/2019.csv | ./splitFileMapper.py | ./splitFileReducer.py
cat `find ./output/intermediate -name '*.csv'` | ./yearlyMapper.py | ./yearlyReducer.py
cat `find ./output/intermediate -name '*-yearly.csv'` | ./reportMapper.py | ./reportReducer.py >> ./output/report.csv