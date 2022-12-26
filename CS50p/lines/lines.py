import sys

def main():
    if input():
        try:
            with open(sys.argv[1]) as file:
                total, whitespace, comment = count_rows(file)
                actuallines = total - whitespace - comment
                print(actuallines)


        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)


def input():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)


    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        if sys.argv[1][-3:] != ".py":
            print("Not a python file")
            sys.exit(1)
        else:
            return True

def count_rows(file):
    counter = 0
    whitespace = 0
    comment = 0
    lines = file.readlines()
    for line in lines:
        counter +=1
        if line.isspace():
            whitespace += 1
        if line.strip().startswith("#"):
            comment += 1
    return counter, whitespace, comment


if __name__ == "__main__":
    main()