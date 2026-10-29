#!/usr/bin/env python3

import sys

# Check if there are at least 2 parameters (len > 2 means script + 2 args)
if len(sys.argv) > 2:
    for param in sys.argv[1:][::-1]:
        print(param)
else:
    print("none")