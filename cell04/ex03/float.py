#!/usr/bin/python3

try:
    number = float(input("Give me a number: "))
    
    print("This number is ", end="")
    if number % 1 != 0:
        print("a decimal.")
    else:
        print("an integer.")
except:
    print("Error")