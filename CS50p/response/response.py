import validators

def main():
    if (validators.email(input("Your email: "))):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()