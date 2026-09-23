#!/usr/bin/env python3
import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    while len(s) < 8:
        s += 'Z'
    print(s)

def main():
    params = sys.argv[1:]
    if len(params) == 0:
        print("none")
        return

    for param in params:
        length = len(param)
        if length > 8:
            shrink(param)
        elif length < 8:
            enlarge(param)
        else:
            print(param)

if __name__ == "__main__":
    main()
