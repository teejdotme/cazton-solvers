#!/usr/bin/env python

import sys

def getStates():
    with open('ghcnd-states.txt', 'r') as file:
        for line in file.readlines():
            yield (line[:2], line[3:].strip())

def main():
    stateNames = {}

    for (state, name) in getStates():
        stateNames[state] = name

    results = []

    for line in iter(sys.stdin.readline, ''):
        (key, entry) = line.strip().split('\t')

        parts = entry.split(',')
        
        state = parts[0]
        minimum = float(parts[1])
        maximum = float(parts[2])
        average = float(parts[3])
        variance = float(parts[4])

        results.append({
            'state': state, 
            'name': stateNames[state],
            'minimum': minimum, 
            'maximum': maximum, 
            'average': average, 
            'variance': variance
        })

    results.sort(key=lambda x: x['variance'])

    print('STATE,NAME,MIN TEMP,MAX TEMP,AVG TEMP,VARIANCE')

    for result in results:
        print(f"{result['state']},{result['name']},{result['minimum']},{result['maximum']},{result['average']},{result['variance']}")
        
main()