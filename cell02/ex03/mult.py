#!/usr/bin/env python3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = num1 * num2
print(num1, "x", num2, "=", result)
if result < 0:
    print("This result is negative.")
elif result == 0:
    print("This result is positive and negative.")
else:
    print("This result is positive.")
