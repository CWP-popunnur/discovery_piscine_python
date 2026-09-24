
import sys
import re

def main():
    
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    text = sys.argv[2]

    
    matches = re.findall(keyword, text)

    if len(matches) > 0:
        print(len(matches))
    else:
        print("none")

if __name__ == "__main__":
    main()
