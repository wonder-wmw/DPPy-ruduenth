#!/usr/bin/env python3

text = input()
result = ""

for char in text:
    if "a" <= char <= "z":
        # Convert lowercase to uppercase by subtracting 32
        result += chr(ord(char) - 32)
    elif "A" <= char <= "Z":
        # Convert uppercase to lowercase by adding 32
        result += chr(ord(char) + 32)
    else:
        result += char

print(result)
