# Christopher Blystone
# 3/1/24
# Project Turtle.
import turtle
# Creating a turtle shape
turtle.shape("turtle")
# Changing the speed of the turtle drawing.
turtle.speed(0)


# Create a line.
def square(len):
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)


square(100)
turtle.Screen().exitonclick()
