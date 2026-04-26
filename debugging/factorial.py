#!/usr/bin/python3
import sys
import os

# Bu hissə fayla icra icazəsi verməyə çalışır
os.chmod(os.path.abspath(__file__), 0o755)

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(factorial(int(sys.argv[1])))
