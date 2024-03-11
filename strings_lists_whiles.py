# Christopher Blystone
# 3/7/2024
# Strings, Lists and Whiles

# Problem 1). Write a function average_neg_evens that takes a list of numbers as a paramerter and adds all the negative even numbers (less than 0 and divisible by 2) together and returns their average.
# Example:                                                  Output
# print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))       -3
def average_neg_evens(numbers):
    sum = 0  # Variable to hold the sum
    count = 0  # Variable to hold the count
    # for num in numbers:
    i = 0  # initializing the loop idex variable
    while i < len(numbers):  # loop condition
        num = numbers[i]  # how we go from index --> value in list
        if num < 0 and num % 2 == 0:
            sum += num
            count += 1
        i += 1  # loop increment
    return sum / count  # Find the average.

# Problem 2). Write a function count_letter that takes a list of strings and a string letter as a parameters and returns the number of times this letter occurs, both upper and lower cased.
# Example
# list = ["HELLO", "goodbye", "1234 Oooh!"]
# print(count_letter(list, "o"))


def count_letter(list, letter):
    count = 0
    letter = letter.lower()
    i = 0  # iterator
    # for item in list:
    while i < len(list):  # iterate through the length of the list
        string = list[i]  # breaking it apart.
        count += string.lower().count(letter)
        i += 1  # counting the iterator.
    return count


def main():
    num = [0, 1, 2, -2, -3, -4, 3, 4]
    print(average_neg_evens(num))
    my_list = ["HELLO", "goodbye", "1234 Oooh!"]
    print(count_letter(my_list, "o"))
    print("End")


main()
