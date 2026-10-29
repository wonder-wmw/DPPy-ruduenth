#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Build a unique set directly using a set comprehension
unique_processed = {num + 2 for num in original_array if num > 5}

print(original_array)
print(unique_processed)