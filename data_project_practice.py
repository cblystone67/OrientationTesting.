# Author: Christopher Blystone
# March 11, 2024
# Writing a program that reads a cvs file and outputs the mean, median, and standard deviation for the fall and spring sememsters.
import csv
import statistics


def output_stats(list):
    print("Mean:   ", statistics.mean(list))
    print("Median: ", statistics.median(list))
    print("STD:    ", statistics.stdev(list))


def reading_file(filename, split=','):
    file = open(filename)
    for line in file:
        list = line.rstrip().split(split)
    file.close()


# Data variables
spring = []
fall = []
csv = "sample_grades.csv"
file = open(csv)
for line in file:
    # print(line.rstrip())
    list = line.rstrip().split(",")
    # print(list)
    if list[1] == "Spring 2016":
        spring.append(int(list[2]))
    else:
        fall.append(int(list[2]))

file.close()
print("Spring: ", spring)
print("Fall:   ", fall)
print("Fall 2016: ")
output_stats(fall)
print()
print("Spring 2016: ")
output_stats(spring)
