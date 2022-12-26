def main():
    grocery = {}

    while True:
        try:
            i = input()
            if i not in grocery:
                grocery[i] = 1
            else:
                grocery[i] += 1

        except EOFError:
            sorted_items = sorted(grocery.items())
            dict(sorted_items)
            for i in range(0, len(sorted_items)):
                print(f"{sorted_items[i][1]} {sorted_items[i][0].upper()}")
            break


if __name__ == "__main__":
    main()