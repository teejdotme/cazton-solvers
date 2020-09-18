#!/usr/bin/env python

import csv
import sys

def getStates():
    with open('input/ghcnd-states.txt', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ')

        for row in csvreader:
            yield row[0]

def getStations():
    with open('input/ghcnd-stations.txt', 'r') as stationfile:
        for line in stationfile.readlines():
            id = line[0:11].strip()
            state = line[38:40].strip()

            if state:
                yield (id, state)

def getReadings():
    csvreader = csv.reader(iter(sys.stdin.readline, ''), delimiter=',')

    keys = ['TMIN', 'TMAX']

    for row in csvreader:
        stationId = row[0]
        date = row[1]
        key = row[2]
        value = float(row[3])

        if not key in keys:
            continue

        if value > 1500 or value < -1500:
            # sanity check
            continue

        yield (stationId, date, key, value)


def main():
    stationsByState = {}
    statesByStation = {}
    
    for item in getStates():
        stationsByState[item] = []

    for (stationId, state) in getStations():
        if not state in stationsByState:
            continue

        stationsByState[state].append(stationId)
        statesByStation[stationId] = state

    for (stationId, date, key, value) in getReadings():
        if not stationId in statesByStation:
            continue

        state = statesByStation[stationId]

        print(f"{state}^{stationId},{date},{key},{value}")

main()