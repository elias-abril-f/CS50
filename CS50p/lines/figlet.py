from pyfiglet import Figlet
    #

import sys
from random import choice
figlet = Figlet()
def main():
    font_list = figlet.getFonts()
    length = len(sys.argv)
    if not length == 1 and not length == 3:
        print("Invalid usage")
        sys.exit(1)
    if length == 3:
        if sys.argv[2] not in font_list or sys.argv[1] != "-f":
            print("Invalid usage")
            sys.exit(2)
    r = input("Input: ")
    if len(sys.argv) == 1:
        f = choice(font_list)
        figlet.setFont(font=f)
        print(figlet.renderText(r))
    if len(sys.argv) == 3:
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(r))
if __name__ == "__main__":
    main()