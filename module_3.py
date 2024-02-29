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

