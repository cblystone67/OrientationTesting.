# Christopher Blystone
# 3/10/2024
# Writing the code for file opperations with dictionaries.
# open()  use the precursers "r"-read, "a"-append, "w"-write, "x"-create
# "t"-for text mode, "b"-for binary mode
# Count the number of letter grades in a file.
letters = ["A", "B", "C", "D", "F"]
counts = {}
file = "letter_grades.txt"
for line in open(file):
    letter = line.replace("\n", "")
    # If commas use the split function
    # Gets the count of letter if it exists, 0 otherwise
    count = counts.get(letter, 0)
    counts[letter] = count + 1  # store count

# print out counts
for l in letters:
    print(l + ":", counts.get(l, 0))

print("Just testing out the dictionary counting")
for item in counts.keys():
    print(item + ":", counts[item])
