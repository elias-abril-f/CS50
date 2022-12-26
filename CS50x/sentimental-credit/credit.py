from cs50 import get_int
ccn = 0
while (type(ccn) != int) or ccn == 0:
    ccn = get_int("Number ")
# ccn = str(ccn)
tmp = 0
sumEven = 0
sumOdd = 0
counter = 1
length = len(str(ccn))
number = ccn
if (length < 13 or length > 16):
    print("INVALID")
else:
    while counter <= length:
        # If the digit is in an odd position
        if ((counter % 2) == 1):
            tmp = ccn % 10
            ccn = ccn // 10
            sumOdd += tmp
            #print(f"Odd {tmp}")
            counter += 1

        # If the digit is in an even position
        else:
            tmp = ccn % 10
            ccn = ccn // 10
            #print(f"Even {tmp} {tmp * 2}")
            if tmp < 5:
                sumEven += tmp * 2
            else:
                sumEven += 1
                sumEven += (tmp * 2) % 10
            counter += 1
        # Do it once more to print the last number
    totalSum = sumEven + sumOdd
    if (totalSum % 10 == 0):
        totalSum = True
        # print(totalSum)
        if (length == 15 and (((number // 10000000000000) == 34) or ((number // 10000000000000) == 37))):
            print("AMEX")

        elif (length == 16 and ((number // 100000000000000) in range(51, 56))):
            print("MASTERCARD")

        elif ((length == 16 and ((number // 1000000000000000) == 4)) or (length == 13 and ((number // 1000000000000) == 4))):
            print("VISA")
        else:
            print("INVALID")

    else:
        print("INVALID")

