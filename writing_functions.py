# Christopher Blystone
# 3/3/24
# writing functions and calling them.

# 1). Write a function called add that takes two numbers as parameters and returns their sum
def add(x, y):
    return x + y
# 2). Write a function, multiply, that takes two numbers as parameters and returns their product.


def multiply(x, y):
    return x * y
# 3).  Collecting a user input to collect the 2 numbers.


def usernumbers():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter another number: "))
    return num1, num2


def caculating():
    choice = input(
        "Please choose which you would like to do either add or multiply: ")
    if (choice == 'add'):
        num1, num2 = usernumbers()
        sum = add(num1, num2)
        print(f"The sume of {num1} plus {num2} equals {sum}")
    elif (choice == "multiply"):
        num1, num2 = usernumbers()
        sum = multiply(num1, num2)
        print(f"The sum of {num1} multiplied by {num2} is: {sum}")
    else:
        print("You didn't make a choice that was offered.")


def main():
    caculating()


main()
