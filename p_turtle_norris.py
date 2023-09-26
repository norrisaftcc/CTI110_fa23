"""
CTI 110
P_TURTLE - Turtle graphics
norrisa
9/26/23
Basic Turtle Graphics
"""
# Set up the turtle
import turtle

t = turtle.Turtle() # create the turtle called 't'

# customize our pen
t.pensize(3)
t.pencolor("darkblue")

# Method 1 - tank controls
# Draw a "T"
t.left(90) # degrees)
t.forward(100)
# the top of the T
t.left(90)
t.forward(50)
t.right(180)
t.forward(100)

# move forward with the pen up
t.penup()
t.forward(100)
t.pendown()
t.pencolor("red")

# Draw an "I"
t.right(90)
t.forward(100)

# draw a circle
t.circle(100, 180)


# Method 2 - goto
# raise the pen
t.penup()
t.pencolor("darkred")
t.goto(0,0)
# lower the pen
t.pendown()
t.goto(-100, -100)
t.goto(100, 100)

