import sys
import inflect

from datetime import date, datetime

inflect = inflect.engine()
def main():
    if output := validate(input("your dob: ")):
        print(f"{output} minutes")



def validate(date_text):
    try:
        datein = datetime.strptime(date_text, "%Y-%m-%d")
        today = date.today()
        diff = today - datein.date()
        diffMins = diff.days * 24 * 60
        output = inflect.number_to_words(diffMins, andword="").capitalize()
        return output

    except ValueError:
        sys.exit("Invalid date, should be YYYY-MM-DD")


if __name__ == "__main__":
    main()