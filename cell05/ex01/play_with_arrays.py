#!/usr/bin/env python3

def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = []
    
    for num in original_array:
        new_array.append(num + 2)
        
    print(f"Original array: {original_array}")
    print(f"New array: {new_array}")

if __name__ == "__main__":
    main()
