# Christopher Blystone
# 3/1/2024
# Create a function that takes a rectangle, octagon and draws a stop sign with the post.
import turtle as t

# Create a helper function to move to next location.


def moveleft(len):
    t.penup()
    t.backward(len)
    t.pendown()


def moveright(len):
    t.penup()
    t.forward(len)
    t.pendown()

# Create a rectangle.


def rectangle(width, height):
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)


def pendesign(color, size):
    t.pencolor(color)
    t.pensize(size)

# Create an octagon.


def octagon(len):
    for i in range(8):
        t.forward(len)
        t.left(45)


def stop(len, color, size):
    pendesign(color, size)
    octagon(len)
    length = len*.375
    width = float(len * .2)
    height = float(len * 2)
    moveright(length)
    rectangle(width, height)


stop(50, "blue", 3)
moveleft(150)
stop(25, "red", 2)
t.Screen().exitonclick()
