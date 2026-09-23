#!/usr/bin/env python3

def find_the_redheads(family):
    # ใช้ filter เพื่อกรองเฉพาะคนที่มีสีผมเป็น "red" โดยเช็คจาก value ของ dictionary
    redheads = filter(lambda name: family[name] == "red", family)
    return list(redheads)

if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))
