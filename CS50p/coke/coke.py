def main():
    due = 50
    accepted = [5, 10, 25]
    while due != 0:
        print(f"Amount due: {due}")
        i = int(input("Insert a coin: "))
        if i in accepted:
            due -= i
            if due < 0:
                due = due * -1
                break
    print(f"Change owed: {due}")


if __name__ == "__main__":
    main()
