def main():
    names = []

    while True:
        try:
            i = input()
            if i not in names:
                names.append(i)
            else:
                names.append(i)
        except EOFError:
            break

    r = "Adieu, adieu, to "
    length = len(names)

    if length == 1:
        r += names[0]

    elif length == 2:
        r += f"{names[0]} and {names[1]}"

    else:
        for i in range(0, length):
            r += names[i]
            if i == length - 2:
                r += f", and {names[(i+1)]}"
                break
            r += ", "

    print(r)


if __name__ == "__main__":
    main()