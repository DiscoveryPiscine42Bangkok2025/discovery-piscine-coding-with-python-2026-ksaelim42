#!/usr/bin/python3

try:
    number = int(input("Enter a number\n"))

    for x in range(13):
        result = number * x;
        print(f"{x} x {number} = {result}")
except:
    print("Error")