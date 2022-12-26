def main():
    while True:
        try:
            z = input("Fraction: ")
            r = check(z)
            r = gauge(r)
            break
        except (ValueError, ZeroDivisionError):
            continue
    print(r)


def check(z):
    x, y = z.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError

    elif x > y:
        raise ValueError
    else:
        r = x/y
        return r


def gauge(r):
    r = round(r * 100)
    if r >= 99:
        r = "F"
    elif r <= 1:
        r = "E"
    else:
        r = (str(r) + "%")
    return r


if __name__ == "__main__":
    main()