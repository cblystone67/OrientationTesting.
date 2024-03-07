# Chistopher Blystone
# 3/6/2024
# Writing Lists and Strings

# Problem 1). Write a program that creates a list of 20 numbers input by the user and prints the average (mean) of the list.
# Problem 2). Write a function mangle that takes a string as a parameter and returns the string after performing the following operations:
#     i. Converting the string to all upper case letters
#     ii. Removing the third character
#     iii. Removing the third to last character.
# Test that your function works.
# Example                    Output
# print(mangle("hellothere"))     HELLOTHERE
# print(mangle("42 degrees Celsius"))   42DEGREES CELSUS
# Print(mangle("eeeeeee"))   EEEEE
def mangle(text):
    workstr = text[:]  # Creates the new string
    workstr = workstr.upper()  # puts it into capitalized characters
    # elliminates the 3 char and the 3 from the last char.
    workstr = workstr[0:2]+workstr[3:-3] + workstr[-2:]
    return workstr
# Problem 3). Write a function, count_e that takes a list of strings as a parameter and returns the total number of upper and lower case e's("E" and "e") in all the strings in the list.
# Example functions call:              output
# print(count_e(["hi", "hello", "EEK!"])) 3


def count_e(my_list):
    num_vowel = 0
    for string in my_list:
        num_vowel += string.upper().count("E")

    return num_vowel
# Problem 4). Write a function, count_vowels, that takes a list of strings as a parameter and returns the total number of upper and lower case vowels(A, E, I, O, U)in all the strings in the list.
# Example                             Output
# print(count_vowels(["hi", "hello", "OOF!"]))                               5
# See Problem 3, using the same principle.  You first have to break out each word, then go through each letter and compare it with the char you are looking for.


def count_vowels2(list):
    num_vowels = 0
    vowels = 'AEIOU'
    for string in list:
        num_vowels += string.upper().count()
    return num_vowels


def count_vowels(my_list):
    vowels = 'AEIOU'
    return len([char for char in my_list if char in vowels])


def main():
    # -----------------------------------------
    # Problem 1).
    # create a variable for the user input
    # create loop to accept the user input and add them to the variable.
    number = []
    for i in range(2):
        number.append(int(input("Please enter a number: ")))
    average = sum(number) / len(number)
    print(average)
    print(number)
    print(len(number))
    print("End of Problem 1")
    # ---------------------------------------
    # Problem 2)
    print(mangle("hellothere"))
    print(mangle("42 degrees Celsius"))
    print(mangle("eeeeeee"))
    print("End of Problem 2")
    # -----------------------------------------
    # Problem 3.
    print(count_e(["hi", "hello", "EEK!"]))
    print(count_e(["stupid", "either", "itterate", "hello"]))
    print("End of Problem 3")
    # Problem 4.
    print(count_vowels(["hi", "hello", "OOF!"]))
    print(count_vowels(["stupid", "either", "itterate", "hello"]))
    print(count_vowels(["people", "at", "home", "everyone", "home"]))
    print("End of Problem 4")
    print("end of main")
    print(count_vowels2(["Hello"]))


main()
