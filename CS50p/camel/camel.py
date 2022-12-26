def main():
    i = input("camelCase: ")
    r = change(i)
    print(r)


def change(i):
    temp = ""
    for i in i:
        if i.isupper():
            temp += "_"
        temp += i.lower()
    return temp


if __name__ == "__main__":
    main()
