# problem a.
# j = 4
# while j > -4:
#     print(j)
#     j -= 1
# problem b.
# string = "Hello"
# builder = ""
# i = 0
# while i < len(string):
#     builder += string[i].swapcase()
#     print(i, builder)
#     i += 1
# print(string, "->", builder)
# problem c.
# x = 0
# i = 1
# while x < 20:
#     if x > 5:
#         x += 15
#     else:
#         x += 1
#     print(i, x)
#     i += 1
# Problem 2.
# problem a.
# string = "HELLO"
# x = 0
# while string[x] != 'L':
#     print(string[x], end="... ")
#     x += 1
# print("\n", string, "first L is at", x)
# Problem b.
# Assume the user enters the following:
# hello goodbye cat dog DONE done
# list = []
# prompt = "Please enter word, 'done' to finish "
# response = input(prompt)
# while response != "done":
#     list.append(response)
#     response = input(prompt)
# print(sorted(list))
# Problem c.
# x = 0
# while x < 20:
#     if x > 5:
#         if x % 2 == 0:
#             x *= 2
#         else:
#             x *= -1
#     else:
#         x += 10
#     x += 1
#     print(x)

# Problem 1). of Writing While Loops
# a.
a = 1
while a <= 5:
    print(a)
    a += 1
print("End of a.")
# b.
b = 2
while b < 12:
    print(b)
    b += 3
print("End of b")
# c.
c = -10
while c <= 0:
    print(c, end=" ")
    c += 2
print()
print("End of c")
# d
d = 0
while d < 0:
    print("*" * 4)
    d += 1
print("End of d")
# Problem 2). Write a while loop that prints the letters in "CSCI 150" on separate lines.

text = "CSCI 150"
letter = 0
while letter < len(text):
    print(text[letter])
    letter += 1
print("End of Problem 2).")
# Problem 3). Create a program that allows the user to enter in a list of numbers, prints them out in sorted order, and prints the sum and average of the numbers.  Prompt the user to continue entering numbers, and enter the number '0' when finished.

# list = []
# prompt = "Please enter a number or numbers to quit enter '0' :"
# response = input(prompt)
# sum = 0
# count = 0
# while response != '0':
#     list.append(response)
#     response = input(prompt)
#     list2 = map(int, list)
#     count += 1

# for i in list2:
#     sum += i
# print(f"The sum of your numbers is: {sum}")
# print(f"The Average of {list} is {sum / count}")
# print("End of Problem 3).")
