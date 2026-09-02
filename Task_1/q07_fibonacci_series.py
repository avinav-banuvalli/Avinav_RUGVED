# Q7-Write a program to print the Fibonacci Sequence till n-values where n is user input

# Function to print Fibonacci number
def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Function to print Fibonacci series
def fibonacci_series(n):
    for i in range(1, n+1):
        # The end = " " is used so that all numbers can be printed in a single line
        print(fibonacci(i), end = " ")
    print()

# Taking input from the user
num = int(input("Enter a number:"))

if num < 0 :
    print("Enter non ngative number")
else:
    fibonacci_series(num)

    