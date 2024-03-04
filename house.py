# Christopher Blystone
# 3/1/2024
# Step 7 in Project Turtle.
import turtle as t


def move(len):
    t.penup()
    t.backward(len)
    t.pendown()


def triangle(len):
    t.sety(len)
    for i in range(3):
        t.forward(len)
        t.left(120)


def square(len):
    for i in range(4):
        t.forward(len)
        t.left(90)
    triangle(len)
    t.sety(len - len)


def picture(len):
    for i in range(4):
        square(len)
        move(len + 10)
        print(i)
        if (i == 0):
            t.pencolor("red")
            t.pensize(i+3)
        elif (i == 1):
            t.pencolor("blue")
            t.pensize(i + 3)
        else:
            t.pencolor("pink")
            t.pensize(i+4)


def main():
    picture(100)


main()
t.Screen().exitonclick()
