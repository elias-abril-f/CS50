import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    all = re.findall(r"\bum\b", s, re.IGNORECASE)
    return (len(all))


if __name__ == "__main__":
    main()