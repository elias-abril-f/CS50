def main():
    i = input("Greeting: ").lower().strip()
    r = value(i)
    print(f"${r}")


def value(i):
    i = i
    if "hello" in i:
        r = 0
    else:
        if i[0] == "h":
            r = 20
        else:
            r = 100
    return r


if __name__ == "__main__":
    main()