#number data type


a=5#integer
print(a,type(a))
a=5.5#float
print(a,type(a))
a=2+5j#complex
print(a,type(a))


#string data type


s='hello@123'#single quote
print(s,type(s))
s="this is string"#double quote
print(s,type(s))
b='''
   hello
   Akash kumar gupta
'''
print(b)#triple quote
s='10'# string kyeki ki ya single quote
print(s,type(s))


#list


l=[10,'AKG',5.5]#index number par kam krata hai list
l[2]=90#mutabel hai mutabel me data ko change kar shkate hai
print(l,type(l))

#tuple
#tuple list se fast hai list sequre bracket me hota hai and tuple round bracke me hota hai tuple inmutabel data type hai
t=(10,20,'hello')# tuple ko round bracket me likhate hai tuple ke ander comma sparate me likha jata hai
#t[1]=235
print(t,type(t))

d=(10)#integer hai
print(d,type(d))

#dictionary 
#Dictionary unorderd collection and key and value ke paire me hota hai dict. withan  kule braces{ }  and mutabel hai dict.key par kam karata hai
d={
    'course_name':'python',
    'course_duration':'2 month'
}
print(d['course_name'])
print(d,type(d))

#set
#set unordered collection and unique element (number duplicates) and duplicates value kon auto matik remove karata hai
#culle braces me hota hai and inmutabel hota ahi

s={10,20,30,10}
print(s,type(s))
