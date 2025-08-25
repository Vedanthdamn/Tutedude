def fact(n):
    x = 1
    if n < 2:
        x = 1
    else:
        x = n * fact(n - 1)
        
    return x
        
n=int(input("Enter a number: "))

print ("Factorial of",n,"is:",fact(n))