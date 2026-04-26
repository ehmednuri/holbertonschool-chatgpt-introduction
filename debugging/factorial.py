#!/usr/bin/python3
chmod +x factorial.py
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(factorial(int(sys.argv[1])))
