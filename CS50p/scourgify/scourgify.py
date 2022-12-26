import sys
import csv
from os.path import exists


def main():
    if input_check():
        table = read_file()
        write_file(table)


def input_check():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        if sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv":
            print(f"{sys.argv[1]} or {sys.argv[2]} not a csv file")
            sys.exit(1)
        else:
            if not exists(sys.argv[1]):
                print(f"Could not read {sys.argv[1]}")
                sys.exit(1)
            else:
                return True


def read_file():
    table = []
    with open(sys.argv[1]) as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["last"], row["first"] = row["name"].split(", ")
            del row["name"]
            table.append(row)
    return table


def write_file(table):
    with open(sys.argv[2], "w") as f:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in table:
            writer.writerow(row)


if __name__ == "__main__":
    main()