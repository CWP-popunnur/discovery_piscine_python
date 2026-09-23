#!/usr/bin/env python3

def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = []

    for num in original_array:
        if num > 5:
            new_array.append(num + 2)

    # ใช้ set เพื่อกรองตัวที่ซ้ำกันออก แล้วแปลงกลับเป็น list
    unique_array = list(set(new_array))

    print(original_array)
    print(unique_array)

if __name__ == "__main__":
    main()
