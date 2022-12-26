import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # check user input
    if times := re.search(r"^(?:[1-9]|1[0-2])(:(?:[0-5][0-9]))? (?:AM|PM) to (?:[1-9]|1[0-2])(?::(?:[0-5][0-9]))? (?:AM|PM)$", s):
        # create dictionaries for storing before and after
        before = {"hour": "", "meridian": ""}
        after = {"hour": "", "meridian": ""}
        # create temp variables for before and after
        beforetemp, aftertemp = times[0].split(" to ")
        # split values of before and after and store in the dictionaries
        before["hour"], before["meridian"] = beforetemp.split(" ")
        after["hour"], after["meridian"] = aftertemp.split(" ")
        # create a list of the dictionaries
        list = [before, after]
        for item in list:
            if ":" in item["hour"]:
                item["hour"], item["minutes"] = item["hour"].split(":")
            else:
                item["minutes"] = "00"
            if int(item["hour"]) == 12 and item["meridian"] == "AM":
                item["hour"] = "0"
            if item["meridian"] == "PM" and item["hour"] != "12":
                item["hour"] = int(item["hour"]) + 12
            if int(item["hour"]) < 10:
                item["hour"] = "0" + item["hour"]

        return (f"{before['hour']}:{before['minutes']} to {after['hour']}:{after['minutes']}")
    else:
        raise ValueError


if __name__ == "__main__":
    main()
