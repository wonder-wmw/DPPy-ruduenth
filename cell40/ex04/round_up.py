#!/usr/bin/env python3

num = float(input("Give me a number: "))

base_int = int(num)

# If the number is greater than its integer part, it has a decimal tail
if num > base_int:
    rounded = base_int + 1
else:
    rounded = base_int
    
print(rounded)
