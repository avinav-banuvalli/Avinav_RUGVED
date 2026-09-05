# Q9-Code to print Pattern

# Taking input from the user
n = int(input("Enter the number of rows"))

# This is for the upper part of the diamond pattern
for i in range(1, n+1):
    for j in range(n-i):
        print(" ",end = "")
    for j in range(i):
        print("*",end = " ")
    print()

# This is for the lower part of the diamond pattern
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ",end = "")
    for j in range(i):
        print("*",end = " ")
    print()

# This is for the upper part of the butterfly pattern
for i in range(1, n+1):
    for j in range(i):
        if j > 0:
            print(" ", end = "")
        print("*",end = "")
    for k in range(4 * (n-i) + 1):
        print(" ",end = "")
    for u in range(i):
        if u > 0:
           print(" ",end = "") 
        print("*",end = "")
    print()

# This is for the lower part of the butterfly pattern
for i in range(n-1, 0, -1):
    for j in range(i):
        if j > 0:
            print(" ",end = "")
        print("*",end = "")
    for k in range(4 * (n-i) + 1):
        print(" ",end = "")
    for u in range(i):
        if u > 0:
            print(" ",end = "")
        print("*",end = "")
    print()

