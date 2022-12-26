def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    temp = ""
    for d in d:
        if d != "$":
            temp = temp + d

    d = float(temp)
    return d


def percent_to_float(p):
    temp = ""
    for p in p:
        if p != "%":
            temp = temp + p
        else:
            continue

    p = float(temp) / 100
    return p


main()
