def showdata():
    print("welcome to Akash")
    
showdata()
showdata()
showdata()
showdata()

#function Arguments
def sum(a,b):
    print(a+b)
sum(20,10)
sum(40,30)

#parameter value
def sum(a,b=1):
    print(a+b)
sum(20)
sum(20+50)
sum(56,78)

#return value
def square(x):
    return x*x,x*2
s=square(5)
print(s)