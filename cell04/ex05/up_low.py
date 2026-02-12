#!/usr/bin/python3

try:
    word = input("")
    for char in word:
        if char.islower():
            print(char.upper(), end="")
        elif char.isupper():
            print(char.lower(), end="")
            
except:
    print("Error")