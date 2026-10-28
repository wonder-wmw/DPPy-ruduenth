#!/usr/bin/env python3

num1 = float(input("Give me the first number: "))
num2 = float(input("Give me the second number: "))

# Define operations with symbols and lambda functions
operations = [
    ("+", lambda a, b: a + b),
    ("-", lambda a, b: a - b),
    ("*", lambda a, b: a * b),
    ("/", lambda a, b: (
            a / b if b != 0 else "Error (Division by zero)"
        ),
    ),

]

for symbol, func in operations:
    print(f"{num1} {symbol} {num2} = {func(num1, num2)}")
