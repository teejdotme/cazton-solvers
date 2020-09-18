#!/usr/bin/env python

import sys

def formatValue(value):
    value = value / 10
    fahrenheit = (value * 9/5) + 32
    
    return round(fahrenheit, 1)

def main():
    for line in iter(sys.stdin.readline, ''):
        (key, entry) = line.strip().split('\t')

        parts = entry.split(',')
        
        state = parts[0]
        minimum = formatValue(float(parts[1]))
        maximum = formatValue(float(parts[2]))
        average = formatValue(float(parts[3]))
        variance = formatValue(maximum - minimum)

        print(f"{state}\t{state},{minimum},{maximum},{average},{variance}")

main()