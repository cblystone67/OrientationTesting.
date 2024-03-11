# Author: Christopher Blystone
# March 11, 2024
# Writing a program that reads a cvs file and outputs the mean, median, and standard deviation for the fall and spring sememsters.
import csv

file = "sample_grades.csv"
# f = open(file, "r")

# print(f.read())
with open(file, "r") as data:
    for line in csv.reader(data):
        for l in line:
            col = l.split(",")
            print("This is collection", col)
        print("This is the line", line)
