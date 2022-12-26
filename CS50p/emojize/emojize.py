import emoji


def main():
    while True:
        i = input("Input: ")
        try:
            r = emoji.emojize(i)
            list = emoji.emoji_list(r)
            if list == []:
                raise ValueError
            break
        except ValueError:
            continue
    print(r)


if __name__ == "__main__":
    main()