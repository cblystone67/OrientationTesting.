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
x = 0
while x < 20:
    if x > 5:
        if x % 2 == 0:
            x *= 2
        else:
            x *= -1
    else:
        x += 10
    x += 1
    print(x)
