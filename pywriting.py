# 1  Def is a key word for defining a function.
# return is the key word that returns some type of data.
# 2 The difference between return and print is that return will allow you to return some type of data to the program where print merely prints the data and it is no longer usable.
# 3. A: x, name, string, n
# B: 5, 4, joe, hi, 10, * 4
# Void functions are hello,
# Fruitful double, quad, repeat, square


# Iteration or loop.
def factorial(N):
    product = 1
    for i in range(2, N+1):
        product *= i
        print(i)
    return product


answer = factorial(5)
print(answer)

# Recursive
# Recursive design
# 1). Program the base case.
# 2). Find the self-similarity.
# 3). Do one step!
# 4). Delegate the rest to recursion.
# Any recursive algorithm can be re-implemented as a loop instead
# -This is an "itertive" expression of the algorithm
# Any loop can be implemented as recursion instead.
# Sometimes recursion is clearer and simpler
# --Mostly for data strauctures with a recursive structure.
# Sometimes iteration is clearer and simpler.


def fac(N):
    if N <= 1:  # Base Case  user must come up with this first.
        return 1
    else:
        # Recursive equation to find your answer. This must have some type of equation and incrementing or decrementing.
        return N*fac(N-1)


factoring = fac(5)
print(factoring)
