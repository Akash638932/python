#create dictionary
d={
    'name':'python',
    'fees':800,
    'Duration':'2 month'

}
#access elements from a dictionary
n=d['name']
print(n)

#iterating through a dictionary
#program:-
d={
    'name':'python',
    'fees':800,
    'duration':'2 month'
}
#print(type(d))
f=d['fees']
print(f)

d={
    'name':'python',
    'fees':8000,
    'duration':'6 months',}
for i in d:
    print(d[i])


#get()
#keys()
#value()
#items()
#del()
#pop()
#dict()
#update()
#clear()

#get()
d={
    'course':'python',
    'fees':8000,
    'duration':'2 month'
}
c=d.get('curse')
print(c)
#or 
c1=d[ 'course']
print(c1)

#keys()
d={
    'course':'python',
    'fees':8000,
    'duration':'2 month'
}
for i in d.Keys():
    print(i)
  
  
#values
d={
    'course':'python',
    'fees': 8000,
    'duration': '2 month'
      
}
for i in  d.values():
    print(i)
    
#items
for a,b in d.items():
    print(a,b)
    
    
#del
d={
    'course':'python',
    'fees':8000,
    'duration':'2 month'
}
del d['fees']
print(d)

#pop()
d={
   'course':'python',
    'fees':8000,
    'duration':'2 month' 
}
print(d.pop('duration'))
print(d)

#dict()
d=dict(name='python',fees=9000)
print(d)

#update()
d={
     'name':'python',
    'fees':8000,
    'duration':'2 month' 
}
d.update({'fees':100000})
print(d)

#clear()
d={
     'course':'python',
    'fees':8000,
    'duration':'2 month' 
}
d.clear()
print(d)