def main():
    i = input("Greeting: ").lower().strip()
    r = check(i)
    print(f"${r}")


def check(i):
    if "hello" in i:
        r = 0
    else:
        if i[0] == "h":
            r = 20
        else:
            r = 100
    return r


main()