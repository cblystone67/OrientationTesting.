# Christopher Blystone
# For Loop Programs

# Problem 1
# A.
for i in range(1, 6):
    print(i)
print("End of A.")
print()
# B.
for i in range(2, 12, 3):
    print(i)
print("End of B")
print()
# C.
for i in range(-10, 1, 2):
    print(i, end=" ")
print("End of C")
print()
# D.
star = "****"
for _ in range(4):
    print(star)

print()

for i in range(4):  # lines
    for j in range(4):  # columns for each row
        print("*", end="")
    print()
print("End of D")
print()
# 2. Write a for loop that prints the letters in "CSCI 150" on separate lines.
word = "CSCI 150"
for i in word:
    print(i)
print("End of 2.")
print()
# her form
for c in "CSCI 150":
    print(c)
print()
# 3 Using the range function, print the numbers from 1 to 10 (inclusive). Each number should be on a separate line.
for i in range(1, 11):
    print(i)
print("End of 3")
print()

# Second Stage to Module 3 learning exercises:
# 1). Loop for multiples of 5 from 10 through 25 inclusive. They should be seperated by a space.
for i in range(10, 26, 5):
    print(i, end=" ")
print()

# 2). Print the multiples of 3 from -3 to 21 inclusive.  Each number should be separated by a comma and a space.  There should not be a comma after the final number (21).
for i in range(-3, 22, 3):
    if (i == 21):
        print(i)
    else:
        print(i, end=", ")
print()
