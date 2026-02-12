#!/usr/bin/python3

try:
    word = input("")
    for char in word:
        if char.islower():
            print(char.upper())
        elif char.isupper():
            print(char.lower())
            
except:
    print("Error")