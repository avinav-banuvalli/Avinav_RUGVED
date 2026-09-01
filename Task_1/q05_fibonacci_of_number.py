def fibonacci(n) :
    if n==1 :
        return 1
    elif n==2 :
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num=int(input("Enter a number: "))

if num<0 :
    print("Enter non negative number")
else :
    print(f"Fibonacci of {num} is {fibonacci(num)}")

        
    
    