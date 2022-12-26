from fpdf import FPDF

# Create a class cause this is what this week's problems are all about...
class Certificate(FPDF):
    def __init__(self, name):
    #initialise all the shit from the FPDF class as well
        super().__init__()
    # Create a new page for our pdf
        self.add_page()
    # Set the font
        self.set_font("helvetica", "B", 50)
	# Create the title
        self.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
    # Add the image
        self.image("shirtificate.png", w=self.epw)
    # Change the font size for the print in the tshirt
        self.set_font_size(30)
    # Change the colour of the text
        self.set_text_color(255, 255, 255)
    # Create the text that goes on the tshirt
        self.text(x=53, y=150, txt=f"{name} took CS50")

# Create the shirtificate object with the class above
shirt = Certificate(input("What's your name?: "))
# Save the certificate
shirt.output("shirtificate.pdf")