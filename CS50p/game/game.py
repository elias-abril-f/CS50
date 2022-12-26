import random


def main():
    level = levelcheck()
    r = random.randint(1, int(level))
    checkguess(r)


def levelcheck():
    l = ""
    while True:
        try:
            l = input("Level: ")
            if l.isdigit() and int(l) >= 1:
                break
        except ValueError:
            continue
    return l


def checkguess(r):
    i = 0
    while i != r:
        i = input("Guess: ")
        try:
            i = int(i)
        except ValueError:
            continue
        if i >= 1 and i <= 100:
            if i > r:
                print("Too large!!")
                continue
            if i < r:
                print("Too small!!")
                continue
    print("Just right!")
    return


if __name__ == "__main__":
    main()