# Christopher Blystone
# Collect a decimal number and give the absolute value, rounded and square root.
import math


num = float(input("Please give me a decimal number: "))

print("absolute value: ", abs(num))
print("rounded to 0: ", round(num, 0))
print("square root: ", math.sqrt(abs(round(num, 0))))
