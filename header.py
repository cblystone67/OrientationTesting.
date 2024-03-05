# Christopher Blystone
# 3/5/2024
# Understanding how to write your own function.

def header(text, boarder):
    print(boarder * (len(text)+4))
    print(boarder, text, boarder)
    print(boarder * (len(text) + 4))


def main():
    header("Hello World!", "*")
    header("Python Rocks", "!")
    header("Coders 4 EVER", "+")
    print("end of main")


main()
