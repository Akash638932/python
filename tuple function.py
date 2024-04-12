# creating atuple
t=(10,20,30,40,60)
n=t[0]
print(n)


t=(10,20,30,40,50)
#print(type(t))
n=t[3]
print(n)

#tuple function
#min()
#max()
#count()
#sum()

#first
t=(10,20,30,40,50)
l=len(t)
for i in range(l):
    print(l)
    print(t[i])

#second
t=(10,20,30,40,50)
for i in t:
    print(i)
#min()
t=(10,20,30,40,50)
m=min(t)
print(m)

#max()
t=(10,20,30,40,50)
m=max(t)
print(m)

#count()
t=(10,20,30,40,50)
n=t.count(10)
print(n)

#index()
t=(10,20,30,40,50)
n=t.index(50)
print(n)

#sum()
t=(10,20,30,40,50)
s=sum(t,10)
print(s)