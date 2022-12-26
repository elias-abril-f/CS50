i = input('-->')

faces = [":)", ":("]
temp = ""
lenght = len(i)
counter = 0
for i in i:
    counter += 1
    temp = temp + i
    if i == " " or counter == lenght:
        if temp == ":)" or temp == ":) ":
            print("🙂 ", end="")
            temp = ""

        if temp == ":(" or temp == ":( ":
            print("🙁 ", end="")
            temp = ""

        else:
            print(temp, end="")
            temp = ""
print("")
