# Christopher Blystone
# Testing Code
import math
from math import sqrt

print("The square root of 25 is", sqrt(25))
print("The log10 of 100 is", math.log10(100))
print("The absolute value of -5 is", abs(-5))

phrase = "find your Yoda"

print(phrase.upper())
print(phrase.title())
print(phrase.count("o"))
print(phrase.lower().islower())
print(phrase.isdecimal())

# Reading If's
# 2
DoW = input("What day is it? ").title()

if DoW == "Saturday":
    print("Wake up at 9 am")
elif DoW == "Sunday":
    print("Wake up at 10 am")
else:
    print("Wake up at 7 am")

x = 3
y = 7

print(not x == 5)
print(x > 0 and y > 0)
print(x < 0 or y < 0)
print(x*y > 20 or x*y < -20)

print(not (x == 0 or y == 5))
print(not x == 0 or y == 5)
print(x == 3 and not y == 5)
print(not (x == 3 and y == 5))
