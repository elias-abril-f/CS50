import sys
from PIL import Image, ImageOps
from os.path import exists, splitext


def main():
    if input_check():
        # open the image to be overlayed
        shirt = Image.open("shirt.png")
        # open the destination
        dest = Image.open(sys.argv[1])
        # crop and center the crop on the destination to match the overlay
        dest = ImageOps.fit(dest, (600, 600), bleed=0.0, centering=(0.5, 0.5))
        # paste the overlay over the destination
        dest.paste(shirt, shirt)
        # save
        dest.save(sys.argv[2])


def input_check():
    formats = [".jpeg", ".png", ".jpg"]
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        try:
            name1, format1 = splitext(sys.argv[1])
            name2, format2 = splitext(sys.argv[2])
            if not (format1.lower() in formats and format2.lower() in formats):
                print(f"Invalid output")
                sys.exit(1)
            if not (format1.lower() == format2.lower()):
                print(f"Input and output have different extensions")
                sys.exit(1)
        except ValueError:
            print("Not the right format")
        else:
            if not exists(sys.argv[1]):
                print(f"Could not read {sys.argv[1]}")
                sys.exit(1)
            else:
                return True


if __name__ == "__main__":
    main()
