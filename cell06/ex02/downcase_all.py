#!/usr/bin/env python3
import sys

def downcase_it(s):
    return s.lower()

def main():
    params = sys.argv[1:]
    if len(params) == 0:
        print("none")
    else:
        for param in params:
            print(downcase_it(param))

if __name__ == "__main__":
    main()
