# Q1-Define a function named “triple_and” that takes three parameters and returns True only if they are all True and False otherwise

# Below defined method accepts three boolean arguments and returns the "and" value of the three arguments
def triple_and(a, b, c):
    return (a and b and c)

# Testing the triple_and method with various values
print(triple_and(True, True, True))
print(triple_and(False, True, True))
print(triple_and(False, False, True))
print(triple_and(False, False, False))