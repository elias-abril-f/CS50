#refactor

def main():
    text = input("Fraction: ")
    percentage = convert(text)
    fuel = gauge(percentage)
    print(fuel)

def convert(fraction):
    while True:
        try:
            nums = fraction.split('/')
            fn = int(nums[0])
            sn = int(nums[1])

            fraction = (fn / sn) * 100


            if fn > sn:
                fraction = input("Fraction: ")

            return int(fraction)

        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError

def gauge(percentage):
    if percentage == 75:
        return "75%"
    elif percentage >= 50 and percentage <= 74:
        return "50%"
    elif percentage >= 25 and percentage <= 49:
        return "25%"
    elif percentage >= 76 and percentage <= 100:
        return "F"
    elif percentage >= 0 and percentage <= 24:
        return "E"

if __name__ == "__main__":
    main()
