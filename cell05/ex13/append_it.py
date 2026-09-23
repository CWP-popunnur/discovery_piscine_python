#!/usr/bin/env python3
import sys

def main():
    params = sys.argv[1:]
    if len(params) == 0:
        print("none")
        return

    for param in params:
        if param.endswith("ism"):
            continue
        print(param + "ism")

if __name__ == "__main__":
    main()
