# Christopher Blystone
# Calculates and prints the average of 10 real numbers entered by the user.
# Make sure to ask the user to enter each number and collecting them after the return.
sum = 0  # aggregator variables must be initialized before the loop.

for i in range(10):
    num = float(input("Please enter a real number: "))
    sum += num

average = sum / 10

print(f"The average of the 10 numbers you entered is: ", average)

