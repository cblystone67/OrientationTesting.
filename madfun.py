# Christopher Blystone
# Collect a decimal number and give the absolute value, rounded and square root.
import math
from math import sqrt

num = float(input("Please give me a decimal number: "))


def madfun(number):
    absNum = abs(number)
    roundNum = round(number)
    if (number < 0):
        number = number * -1
        squrNum = sqrt(number)
    else:
        squrNum = sqrt(number)
    print(absNum)
    print(roundNum)
    print(squrNum)


madfun(num)
