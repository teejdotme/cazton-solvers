#!/usr/bin/env python

import sys

def main():
    resultsByState = {}

    for line in iter(sys.stdin.readline, ''):
        parts = line.strip().split(',')
        
        state = parts[0]
        #stationId = parts[1]
        date = parts[2]
        key = parts[3]
        value = float(parts[4])

        if not state in resultsByState:
            resultsByState[state] = {}

        if not date in resultsByState[state]:
            resultsByState[state][date] = {
                'min': None,
                'max': None
            }

        results = resultsByState[state][date]

        if key == 'TMIN':
            if not results['min']:
                results['min'] = value
            else:
                results['min'] = min(results['min'], value)

        if key == 'TMAX':
            if not results['max']:
                results['max'] = value
            else:
                results['max'] = max(results['max'], value)

    for state in resultsByState.keys():
        for (date, results) in sorted(resultsByState[state].items()):
            results = resultsByState[state][date]

            average = (results['min'] + results['max']) / 2

            print(f"{state},{date},{results['min']},{results['max']},{average}")

main()