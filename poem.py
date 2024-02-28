# Christopher Blystone
# Collect two words from the user and use them in a poem
fword = input("Please give me a plural noun: ")
sword = input("Please give me a adjective: ")


def poem(first, second):
    first = first.title()
    second = second.lower()
    print(first, "are red, violets are blue Monty Python is", second, "woo hoo!")


poem(fword, sword)
