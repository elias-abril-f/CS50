def main():
    x, y, z = input("Expression (x y z) where y is the operators: ").split(" ")
    x = float(x)
    z = int(z)

    r = check(x, y, z)
    print(r)


def check(x, y, z):
    if y == "/" and z == 0:
        r = ("Try again,you cheeky fucker")

    elif y == "+":
        r = x+z

    elif y == "-":
        r = x-z

    elif y == "*":
        r = x*z

    elif y == "/":
        r = x/z

    return r


if __name__ == "__main__":
    main()
