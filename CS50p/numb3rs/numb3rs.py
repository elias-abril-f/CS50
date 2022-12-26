import re
import sys


def main():
    i = input("IPv4 Address: ")
    b = validate(i)
    print(b)


def validate(ip):
    if re.search(r"^((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()