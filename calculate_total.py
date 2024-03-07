# Christopher Blystone
# 3/5/2024
# Problem 5).  Write a function calculate_total that takes 3 parameters:
# a. meal: The cost of the meal
# b. tax_rate: the percent tax (e.g. NJ tax would be 0.07)
# c. tip_rate: the percent tip (e.g., a 20% tip rat is 0.20)
# Proper tipping technique dictates that the tip should be calculated based on the total cost of the meal, before tax is applied.  Then return the total.  Teest your function works by using the following call:
# calculate_total(53.48, .07, .18) Should return $66.85

def calculate_total(meal, tax, tip):
    taxTotal = meal * tax
    tipTotal = meal * tip
    total = meal + taxTotal + tipTotal
    return total  # , taxTotal, tipTotal


# Problem 6).  Write a function called hey that takes a number as a parameter, squares it, and outputs the parameter squared
# Example call                  Return
# hey(5)                         25
# hey(0)                         0
# hey(-3)                         9

def hey(number):
    return number ** 2

# problem 7). Write a function there that takes a number n as a parameter and returns 2n if n is positive and 0 otherwise.  Your function should output the following for the given calls.
# example call                    return
# there(5)                           32
# there(0)                            1
# there(3)                            8
# there(-2)                           0
# there(-6)                           0


def there(n):
    if (n < 0):
        return 0
    return n ** 2


# Problem 8). Write a function are_we that takes a number of times to repeat a phrase to be repeated as a parameter and outputs the following for the give calls.
# Example call                    Prints
# are_we(2, "there") Are we there yet? Are we there yet?
# are_we(3, "50")  Are we 50 yet? Are we 50 yet?  Are we 50 yet?
# are_we(1, "") Are we  yet?
# are_we(0, "hey")

def are_we(num, text):
    if (num != 0):
        for i in range(num):
            print(f"Are we {text} yet?", end=" ")
    else:
        print()
    print()


def main():
    # total, taxTotal, tipTotal = calculate_total(53.48, .07, .18)
    """print(
        f"Your tip came to {tipTotal:.2f} and your tax on your bill was {taxTotal:.2f} bringing your full bill to {total:.2f}")"""
    print(f"Your bill total is: ${calculate_total(50.48, .08, .15):.2f}")
    print(f"Your bill total is: ${calculate_total(53.48, .07, .18):.2f}")
    print(f"Your bill total is: ${calculate_total(105.48, .085, .18):.2f}")
    print(hey(5))
    print(hey(0))
    print(hey(-3))
    print(there(5))
    print(there(0))
    print(there(3))
    print(there(-2))
    print(there(-6))
    are_we(2, "there")
    are_we(3, "50")
    are_we(1, "")
    are_we(0, "hey!")


main()
