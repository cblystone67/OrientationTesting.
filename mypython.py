import turtle

a = 100

t = turtle.Turtle()
t.color = ("blue")

"""for <loop variable> in <sequence>:
      # do repeated code 
This is a for loop.  Loop Variable: variable that gets assigned the next value in sequence at every repetition of the loop
Sequence: can be either Characters in a string, Range of numbers, Items in a list, Lines in a file.
Repeated code: code that gets executed at every repetition of the loop, likely uses the loop variable."""
for i in range(3):
    t.forward(a)
    t.right(120)

"""Functions: Named group of code statements
Makes your program easier to read, test, and debut
Simplify testing and debugging
test & debug simpler individual functions one at a time before testing your program is working as a whole.
Reuse!
Once written & debugged, can be reused
Eliminate repetitive code
Make changes in only one place (DRY)
"""
