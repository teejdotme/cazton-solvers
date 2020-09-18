#!/usr/bin/env python

import sys

def makeOutput(state):
    file = open(f"output/intermediate/readings-{state}.csv", 'w')

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
    stateOutputs = {}

    for line in sys.stdin:
        parts = line.split('^')
        state = parts[0].strip()
        entry = parts[1].strip()

        if not state in stateOutputs:
            stateOutputs[state] = makeOutput(state)

        stateOutputs[state]['writeLine'](f"{state},{entry}")

    for key in stateOutputs.keys():
        stateOutputs[key]['close']()

main()