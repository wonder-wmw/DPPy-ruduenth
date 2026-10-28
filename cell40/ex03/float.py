#!/usr/bin/env python3

num = float(input("Give me a number: "))

# If converting to int doesn't change its numerical value
if num == int(num):
    print("This number is an integer.")
else:
    print("This number is a decimal.")
