#!/usr/bin/env python3
import sys

def main():
    # ตรวจสอบว่าพารามิเตอร์มีน้อยกว่า 2 ตัวหรือไม่ (sys.argv[0] คือชื่อไฟล์สคริปต์)
    if len(sys.argv) < 3:
        print("none")
    else:
        # วนลูปย้อนหลังจากตัวสุดท้ายมาจนถึงตัวแรก (ข้าม sys.argv[0])
        for param in reversed(sys.argv[1:]):
            print(param)

if __name__ == "__main__":
    main()
