#creat a set
s=(10,20,30,40)
print(s)
#iterating througth a set
s=(10,20,30,40)
for i in s:
    print(i)
    
    
#note:-it the item to removes does not exit
#removes() will raise an error
 #remove
s=[10,20,30,40,50] 
s.remove(20)
print(5)


#discard()
#note:- if the item to remove does note exit discard() will npt raise an error
#pop()
#clear()
#add()
#update()


#set()
l=[10,20,30,40]
s=set(l)
print(s)

#remove()
l=[10,20,30,40,50]
s.remove(20)
print(s)

#discard()
l=[10,20,30,40,50]
s.discard(30)
print(s)

#pop()
l=[10,20,30,40,50]
#s.pop()
#print(s)
print(s.pop())
print(s.pop())
print(s)

#clear()
l=[10,20,30,40,50]
s.clear()
print(s)

#add()
l=[10,20,30,40,50]
s.add(50)
print(s)

#update()
l=[10,20,30,40,50]
s={10,20,30,40,50}
s.update(l)
print(s)

