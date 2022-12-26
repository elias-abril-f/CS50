def main():
    i = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    r = checkinput(i)
    print(r)


def checkinput(i):
    if i == "42" or i == "forty-two" or i == "forty two":
        r = "Yes"
    else:
        r = "No"
    return r

cd
main()