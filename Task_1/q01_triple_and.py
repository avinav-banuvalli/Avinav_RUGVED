def triple_and(a, b, c):
    return (a and b and c)

print(triple_and(True, True, True))
print(triple_and(False, True, True))
print(triple_and(False, False, True))
print(triple_and(False, False, False))