import random


def main():
    l = get_level()
    t = loop(l)
    print(f"Score: {t}")


def loop(l):
    total = 0
    for i in range(10):
        errors = 0
        x, y = generate_integer(l)
        z = x + y
        while True:
            try:
                i = input(f"{x} + {y} = ")
                if not int(i) == z:
                    print("EEE")
                    errors += 1
                    if errors == 3:
                        print(f"{x} + {y} = {z}")
                        break
                    continue
                total += 1
                break
            except ValueError:
                continue
    return total


def get_level():
    l = ""
    while True:
        try:
            l = input("Level: ")
            if l.isdigit() and int(l) >= 1 and int(l) <= 3:
                break
        except ValueError:
            continue
    return l


def generate_integer(level):
    if level == "1":
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == "2":
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


if __name__ == "__main__":
    main()