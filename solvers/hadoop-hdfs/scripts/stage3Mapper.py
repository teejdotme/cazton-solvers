#!/usr/bin/env python

import sys

def main():
    for line in iter(sys.stdin.readline, ''):
        (key, entry) = line.strip().split('\t')

        print(f"0\t{entry}")
        
main()