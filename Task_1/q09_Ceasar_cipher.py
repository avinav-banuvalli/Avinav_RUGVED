n=int(input("Enter the number of rows"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1,n+1):
    for j in range(i):
        if j>0:
            print(" ", end="")
        print("*",end="")
    for k in range(4*(n-i)+1):
        print(" ",end="")
    for u in range(i):
        if u>0:
           print(" ",end="") 
        print("*",end="")
    print()

for i in range(n-1,0,-1):
    for j in range(i):
        if j>0:
            print(" ",end="")
        print("*",end="")
    for k in range(4*(n-i)+1):
        print(" ",end="")
    for u in range(i):
        if u>0:
            print(" ",end="")
        print("*",end="")
    print()

