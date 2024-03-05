# Christopher Blystone
# 3/5/2024
# Writing person functions
# Absolute dirrence of two numbers

def absolute_difference(num1, num2):
    diff = abs(num1 - num2)
    return diff


def main():
    print("difference 5 10", absolute_difference(5, 15) == 10)
    print("difference 200 -200", absolute_difference(200, -200) == 400)
    print("difference 10 5", absolute_difference(10, 5) == 5)
    print("difference 5 10", absolute_difference(5, 10) == 5)
    print(absolute_difference(8, 4))


main()
