import sys
import csv

from tabulate import tabulate
from os.path import exists


def main():
    if input():
        wijth open(sys.argv[1]) as file:
            table = []
            reader = csv.DictReader(file)
            for row in reader:
                table.append(row)
            print(tabulate(table, headers="keys", tablefmt="grid"))


def input():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        if sys.argv[1][-4:] != ".csv":
            print("Not a csv file")
            sys.exit(1)
        else:
            if not exists(sys.argv[1]):
                print("File does not exist")
                sys.exit(1)
            else:
                return True


if __name__ == "__main__":
    main()