#!/usr/bin/env python3

t1 = float(input())
t2 = float(input())

mult = t1*t2
print(f"{t1} x {t2} = {mult}")

if(mult == 0):
    print("The result is positive and negative.")
elif mult > 0:
    print("The result is positive")
else:
    print("The result is negative")