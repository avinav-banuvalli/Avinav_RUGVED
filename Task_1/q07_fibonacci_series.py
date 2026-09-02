def fibonacci(n):
    if n==0 :
        return 0
    elif n==1 :
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_series(n):
    for i in range(1,n+1):
        print(fibonacci(i), end=" ")
    print()

num=int(input("Enter a number:"))

if num<0 :
    print("Enter non ngative number")
else:
    fibonacci_series(num)

    