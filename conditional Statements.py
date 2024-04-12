#if statements 
#me jab true hoga print kare gi And jab false hoga empty print kare gi
a=int(input("Enter the number:-"))
if a%2==0:
   print(a,"Even number")
   
   
#if else statements
   
a=int(input("Enter the number:-"))
if a%2==0:
   print(a,"Even number")#true
else:
    print(a,"odd number")  #false 
    
#if elif else statements
per=int(input("Enter the value:-"))
if per>=60:
       print("first div")# pahala true hoga to yaha hi print hoga 
elif per>=40:
       print("second div")#pahala false hoga to yaha print hoga  true hoga to  
elif per>=35:
       print("third div") #pahala and dushara false hoga to yaha print hogaga   true hoga to
else:
        print("fail")#flase print hoga
    
    
    