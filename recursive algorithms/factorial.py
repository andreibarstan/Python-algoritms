def factorial(n):
    if n==0: #base case
        return 1
    else:
        return n* factorial(n-1) # recursive call of function
        
num=int(input("Enter a number: "))
print(f"{num}! = {factorial(num)}") #output format
