# By: Christopher Blystone
# Second Stage to Module 3 learning exercises:

# 1). Loop for multiples of 5 from 10 through 25 inclusive. They should be seperated by a space.
for i in range(10, 26, 5):
    print(i, end=" ")
print()

# 2). Print the multiples of 3 from -3 to 21 inclusive.  Each number should be separated by a comma and a space.  There should not be a comma after the final number (21).
# One of her outcomes.
for i in range(-3, 21, 3):
    print(i, end=", ")
print(i + 3)
# I used an if statement to check for 21.
for i in range(-3, 22, 3):
    if (i == 21):
        print(i)
    else:
        print(i, end=", ")


saying = "howdy"
for u in saying.upper():
    print(saying, end="!!")
print()

x = 0
y = 0
for i in range(5):
    x += int(input("Please enter a number: "))
    y += 1
print(x/y)
