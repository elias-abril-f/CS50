from cs50 import get_int
height = 0

# Loop until you get a number between 1 and 8
while height > 8 or height < 1:
    height = get_int("Height: ")

# Now print the spaces, the hashes double space and the other side of the hashes
for i in range(height):
    print(" " * (height - (i + 1)), end=(""))
    print("#" * (i + 1), end=(""))
    print("  ", end=(""))
    print("#" * (i + 1))
