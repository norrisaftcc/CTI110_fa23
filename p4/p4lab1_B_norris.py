# CTI 110
# P4LAB1 - Part B
# Text "graphics"
# norrisa
# 10/5/23

# Draw a rectangle with text
CHAR = "👾"
#print(CHAR)

# Part 1: Draw a horizontal line
#WIDTH = 6
#HEIGHT = 4
WIDTH = int(input("How wide is the rectangle?"))
HEIGHT = int(input("How tall is it?"))

print("printing", WIDTH, "columns")
for column in range(WIDTH):
    #don't go to a newline
    print(CHAR, end="")
print()

# Part 2: Vertical line
for row in range(HEIGHT):
    print(CHAR) # we want the newline
print()

# Part 3: Draw the rectangle

for row in range(HEIGHT):
    for column in range(WIDTH):
        print(CHAR, end="")
    print() # end the line
