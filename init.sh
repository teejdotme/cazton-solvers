#!/bin/bash

mkdir -p data
curl ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2019.csv.gz > data/2019.csv.gz
curl ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt > data/ghcnd-stations.txt
curl ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-states.txt > data/ghcnd-states.txt