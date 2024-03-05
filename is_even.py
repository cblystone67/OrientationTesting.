# Christopher Blystone
# 3/5/2024
# Problem 4). Write a function is_even that takes a number as a parameter and returns whether or not it is even.  Test that your function works by calling it twice, once with an even number and once with an odd number, and print the results.

def is_even(number):
    return number % 2 == 0


def main():
    print(is_even(1))
    print(is_even(2))
    print(is_even(3))
    print(is_even(4))


main()
