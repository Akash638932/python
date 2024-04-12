def factorial(n):
    if(n==0):
        return 1
    else:
        x=n * factorial (n-1)
        return x
s=int(input("Enter the  number"))
d=factorial(s)
print("Enter the factorial %d"%d)