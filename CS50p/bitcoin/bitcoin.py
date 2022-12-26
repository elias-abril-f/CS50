import sys
import requests

# https://api.coindesk.com/v1/bpi/currentprice.json,


def main():
    i = user_input()
    r = request(i)
    print(f"${r:,.4f}")

def user_input():
    try:
        if len(sys.argv) == 2:
            input= float(sys.argv[1])
            return input

        else:
            print("Missing command-line argument")
            sys.exit(1)
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

def request(i):
    try:
        # make the api query, if succesful, save the json sent into the varible
        foo = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        # get the rate from the json file by accessing the recursive dictionaries, rate inside usd inside bpi.
        rate = float((foo["bpi"]["USD"]["rate_float"]))
        price = rate * i
        return price

    except requests.RequestException:
        print("Unable to fetch the current price. Try again later")
        sys.exit(3)

if __name__ == "__main__":
    main()