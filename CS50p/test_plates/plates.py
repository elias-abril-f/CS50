def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # create is number to check if numbers have been used before
    isnumber = False
    # check if the input is the right length, is only alphanumeric and the first two characters are letters
    if len(s) >= 2 and len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        # for every character form 3 to the end
        for s in s[2:len(s)]:
            # check if its a number
            if s.isdigit():
                # check if its the first number (since the number check is stil neg)
                if not isnumber:
                    # check if its a 0
                    if s != "0":
                        # if not a 0, accept it anc change the number check to indicate that the next numbers are not the first
                        isnumber = True
                    else:
                        # if is a 0, the plate is invalid
                        return False
                        # if the character is a letter and numbers were used before the plate is invalid
            elif s.isalpha() and isnumber:
                return False
    else:
        return False

    return True


if __name__ = "__main__":
    main()