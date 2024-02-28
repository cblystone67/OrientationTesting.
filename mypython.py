import turtle

a = 100

t = turtle.Turtle()
t.color = ("blue")

"""for <loop variable> in <sequence>:
      # do repeated code 
This is a for loop.  Loop Variable: variable that gets assigned the next value in sequence at every repetition of the loop
Sequence: can be either Characters in a string, Range of numbers, Items in a list, Lines in a file.
Repeated code: code that gets executed at every repetition of the loop, likely uses the loop variable."""
"""
for i in range(3):
    t.forward(a)
    t.right(120)
"""
"""Functions: Named group of code statements
Makes your program easier to read, test, and debut
Simplify testing and debugging
test & debug simpler individual functions one at a time before testing your program is working as a whole.
Reuse!
Once written & debugged, can be reused
Eliminate repetitive code
Make changes in only one place (DRY)
def function_name(parameter_names):
    # function body
step 1. Write the code for one example and test it.
step 2. Replace any repeated or changing values with variables.
step 3. Identify parameters (which variables will change every call)
step 4. Write the function signature (name & parameters)
step 5. Write function body (sub parameter names for variables).
step 6. Test! Output should be the same for one example.
step 7. Test some more! Call 2 or 3 more times in same program run.
"""


def back(len):
    t.penup()
    t.backward(len)
    t.pendown()


def move(len):
    back(-1 * len)


def polygon(num, size):
    if (num < 3):
        print("You need at least 3 sides")
    for i in range(num):
        t.forward(size)
        t.left(360/num)


def spiral(len, angle):
    for i in range(len, 5, -5):
        t.forward(i)
        t.right(angle)


spiral(75, 45)
move(150)
spiral(100, 90)

turtle.mainloop()
number = [1, 2, 3, 4, 5]
