#!/usr/bin/env python

import sys

def main():
    resultsByState = {}

    for line in iter(sys.stdin.readline, ''):
        (key, entry) = line.strip().split('\t')

        parts = entry.split(',')

        state = parts[0]
        # date = parts[1]
        minimum = float(parts[2])
        maximum = float(parts[3])
        average = float(parts[4])

        if not state in resultsByState:
            resultsByState[state] = {}

        results = resultsByState[state]

        if not 'min' in results:
            results['min'] = minimum
        else:
            results['min'] = min(results['min'], minimum)

        if not 'max' in results:
            results['max'] = maximum
        else:
            results['max'] = max(results['max'], maximum)

        if not 'avg' in results:
            results['avg'] = []

        results['avg'].append(average)

    for state in resultsByState.keys():
        results = resultsByState[state]

        average = round(sum(results['avg']) / len(results['avg']), 2)

        print(f"{state}\t{state},{results['min']},{results['max']},{average}")
        
main()