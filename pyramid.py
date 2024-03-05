# Christopher Blystone
# 3/5/2024
# Writing functions that creates a pyramid using two parameters on is a character and the second is a number for the rows.


def pyramid(char, number):
    for i in range(1, number + 1):
        print(char * i)


def main():
    print('pyramid("#", 2)')
    pyramid("*", 2)
    print('pyramid("+", 5)')
    pyramid("+", 5)
    print('pyramid("x", 10)')
    pyramid("x", 10)


main()
