def main():
    i = input("Input: ")
    r = shorten(i)
    print(f"Output: {r}")


def shorten(i):
    vowels = ["a", "e", "i", "o", "u"]
    temp = ""
    for i in i:
        if i.lower() not in vowels:
            temp += i

    return temp


if __name__ == "__main__":
    main()
