#!/usr/bin/python3

try:
    number = float(input("Give me a number: "))
    
    if number % 1 != 0:
        number += 1
    print(int(number))
except:
    print("Error")