

def count_uniq(str):
    d = {}  # This is for using a dictionary
    # d = set()  # A set can be used, because all you want is the key which is a number
    for char in str:
        d[char] = 1  # This is for the dictionary
        # d.add(char)  # This is for the set and adding our key to the set.
    return len(d)


def main():
    list = []
    f = open("sample_grades.csv")
    for line in f:
        list.append(line)
        print(list)
    f.close()
    print(list[:2])  # First two lines in the list
    print(list[-2:])  # Last two lines in the list
    print(len(list))  # The number of lines in the list
    # print(count_uniq("111224446"))
    # print(count_uniq("30444775555"))
    # print(count_uniq(""))
    print("End of main")


main()
