# Christopher Blystone
# 3/1/24
# Project Turtle.
import turtle as t


# Creating a variable for turtle.


# Step 1. Create a line.
# t.forward(100)

# Step 2. Create a square, Change its color, make the line thicker, change the speed the turtle draws.
# t.pencolor("blue")
# t.pensize(3)
# t.speed(8)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# Step 3. Draw 2 squares on the screen.  Don't let them connect.
# t.pencolor("blue")
# t.pensize(3)
# t.speed(8)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.penup()
# t.backward(150)
# t.pendown()
# t.pencolor("red")
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# Step 4.  Create a Square function.  Should take the length of each side as a parameter and draws the square using the turtle.
def square(size):
    t.shape("turtle")
    for i in range(4):
        t.forward(size)
        t.left(90)

# square(50)

# Step 5. Create a rectangel function that takes a width and height parameter and uses it to draw a rectangle.


def rectangle(width, height):
    t.shape("turtle")
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# rectangle(100, 50)
# Step 6.  Draw a picture using your newly created square and rectangle functions, draw an interesting picture using a for loop that calls rectangle and or square.  Should call both at least once.


def moveback(len):
    t.penup()
    t.backward(len)
    t.pendown()


def moveforward(len):
    t.penup()
    t.forward(len)
    t.pendown()


def picture():
    for i in range(10, 200, 10):
        square(i)
        moveback(i)
        rectangle(i+30, i)
        moveforward(i+3)


picture()


# Create a helper function to move the square without leaving a line.
# Helper function to collect the pencolor, pensize, drawing speed.


# def square(color, size, speed, length):
#     t.pencolor(color)
#     t.pensize(size)
#     t.speed(speed)
#     for i in range(4):
#         t.forward(length)
#         t.right(90)


# square("blue", 3, 12, 75)
# move(170)
# square("red", 3, 100, 75)

# This allows the screen to stay open until you click on it.
t.Screen().exitonclick()
