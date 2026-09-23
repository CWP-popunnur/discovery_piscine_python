#!/usr/bin/env python3
import sys

def main():
    # sys.argv[0] คือชื่อไฟล์สคริปต์ เราจึงใช้ len(sys.argv) - 1 เพื่อเช็คจำนวนพารามิเตอร์จริง
    num_params = len(sys.argv) - 1
    print(f"Number of parameters: {num_params}.")

if __name__ == "__main__":
    main()
