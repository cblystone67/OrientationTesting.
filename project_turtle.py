# Christopher Blystone
# 3/1/24
# Project Turtle.
import turtle as t

# Creating a turtle shape
t.shape("turtle")
# Creating a variable for turtle.


# Step 1. Create a line.
# turtle.foward(100)

# Step 2. Create a square, Change its color, make the line thicker, change the speed the turtle draws.
# t.pencolor("blue")
# t.pensize(3)
# t.speed(8)
# t.foward(100)
# t.left(90)
# t.foward(100)
# t.left(90)
# t.foward(100)
# t.left(90)
# t.foward(100)
# t.left(90)


# Step 3. Draw 2 squares on the screen.  Don't let them connect.
# Create a helper function to move the square without leaving a line.
# Helper function to collect the pencolor, pensize, drawing speed.
# t.pencolor("blue")
# t.pensize(3)
# t.speed(8)
# t.foward(100)
# t.left(90)
# t.foward(100)
# t.left(90)
# t.foward(100)
# t.left(90)
# t.foward(100)
# t.left(90)
# t.penup()
# t.backward(150)
# t.pendown()

def move(len):
    t.penup()
    t.backward(len)
    t.pendown()


def square(color, size, speed, length):
    t.pencolor(color)
    t.pensize(size)
    t.speed(speed)
    for i in range(4):
        t.forward(length)
        t.right(90)


square("blue", 3, 12, 75)
move(170)
square("red", 3, 100, 75)

t.Screen().exitonclick()
