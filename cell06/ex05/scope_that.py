#!/usr/bin/env python3

def add_one(nb):
    nb += 1
    return nb

def main():
    my_var = 42
    print(f"Before method: {my_var}")
    add_one(my_var)
    print(f"After method: {my_var}")

if __name__ == "__main__":
    main()
