def main():
    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    while True:
        try:
            i = input("Date: ").title().strip()
            y, m, d = check(i, months)
            break
        except ValueError:
            continue

    print(f"{y}-{m}-{d}")


def check(i, months):
    try:
        m, d, y = i.split("/")
        if int(m) > 12:
            raise ValueError
        if int(m) < 10:
            m = "0" + m

    except ValueError:
        if not "," in i:
            raise ValueError
        i = i.replace(',', '')
        m, d, y = i.split(" ")
        if m not in months:
            raise ValueError
        m = months[m]

    if int(d) > 31:
        raise ValueError

    if int(d) < 10:
        d = "0" + d
    return y, m, d


if __name__ == "__main__":
    main()