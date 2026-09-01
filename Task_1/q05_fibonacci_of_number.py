# Q5-Find the fibonacci of a given number using recursion.

#Function to find the fibonacci number
def fibonacci(n) :
    if n==1 :
        return 1
    elif n==2 :
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Taking input from user
num=int(input("Enter a number: "))

if num<0 :
    print("Enter non negative number")
else :
    print(f"Fibonacci of {num} is {fibonacci(num)}")



        
    
    