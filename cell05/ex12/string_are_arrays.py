#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return
    
    text = sys.argv[1]
    z_count = text.count('z')
    
    if z_count > 0:
        print('z' * z_count)
    else:
        print("none")

if __name__ == "__main__":
    main()
    
