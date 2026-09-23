
import sys
import re

def main():
    # ต้องมีพารามิเตอร์ส่งเข้ามาพอดี 2 ตัว (ไม่รวมชื่อไฟล์)
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    text = sys.argv[2]

    # ใช้ re.findall เพื่อค้นหาคำที่ตรงกันทั้งหมดในข้อความ
    matches = re.findall(keyword, text)

    if len(matches) > 0:
        print(len(matches))
    else:
        print("none")

if __name__ == "__main__":
    main()
