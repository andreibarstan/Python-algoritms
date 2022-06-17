def fibonacciRecursive (n):
    if n==0: #base case
        return 0
    elif n==1:#base case
        return 1
    else:
        return fibonacciRecursive(n-1)+fibonacciRecursive(n-2) #recursive call

num = int(input("Enter a number: "))

print (f"The fibonacci number for {num} is {fibonacciRecursive(num)}")
