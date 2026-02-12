#!/usr/bin/python3

try:
    age = int(input("Please tell me your age: "))
    print(f"You are currently {age} years old.")

    for x in range(10, 31, 10):
        print(f"In {x} years, you'll be {age + x} years old.")
except:
    print("Recieve only integer :(")