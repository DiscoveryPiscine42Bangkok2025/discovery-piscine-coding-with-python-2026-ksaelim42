#!/usr/bin/env python3
import sys

try:
    if sys.argv[1]:
        print("none")
except:
    for x in range(11):
        print(f"Table de {x}: ", end="")
        for y in range(11):
            print(x * y, end= " ")
        print();