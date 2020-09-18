#!/usr/bin/env python

import sys

def makeOutput(state):
    file = open(f"output/intermediate/readings-{state}-yearly.csv", 'w')

    def writeLine(line):
        file.write(f"{line}\n")

    def close():
        file.flush()
        file.close()

    return {
        'writeLine': writeLine,
        'close': close,
    }

def main():
    resultsByState = {}

    for line in iter(sys.stdin.readline, ''):
        parts = line.strip().split(',')

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

    stateOutputs = {}

    for state in resultsByState.keys():
        results = resultsByState[state]

        average = round(sum(results['avg']) / len(results['avg']), 2)

        if not state in stateOutputs:
            stateOutputs[state] = makeOutput(state)

        stateOutputs[state]['writeLine'](f"{state},{results['min']},{results['max']},{average}")

    for key in stateOutputs.keys():
        stateOutputs[key]['close']()
        
main()