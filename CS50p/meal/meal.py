def main():
    time = input("What time is it? ")
    h, m = convert(time)
    r = check(h, m)
    print(r)


def convert(time):
    h, m = time.split(":")
    h = int(h)
    m = int(m)
    return h, m


def check(h, m):
    temp = ""
    if h == 7:
        temp = "breakfast time"
    if h == 12 or (h == 13 and m == 0):
        temp = "lunch time"
    if h == 18:
        temp = "dinner time"
    return temp


if __name__ == "__main__":
    main()