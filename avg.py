# Christopher Blystone
# Calculates and prints the average of 10 real numbers entered by the user.
# Make sure to ask the user to enter each number and collecting them after the return.
sum = 0
entries = int(
    input("Please list the number of entries you would like to enter: "))
for i in range(entries):
    num = float(input("Please enter a real number: "))
    sum += num

average = sum / entries

print(f"The average of the {entries} numbers you entered is: ", average)
