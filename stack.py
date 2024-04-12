l=[ ]
while True:
   c=int(input('''
               1.push Elements
               2. pop Elements
               3.peek Elements
               4.display stack
               5.Exit
               '''))
   if c==1:
       n=input("Enter the value:-")
       l.append(n)
       print(l)
   if c==2:
        if len(l)==0:
            print("Empty stack:-")
        else:
            p=l.pop()
            print(p)
            print(l)
   elif c==3:
        if len(l)==0:
            print("Empty stack:-")
        else:
            print("last stack value",l[-1])
   elif c==4:
       print("display",l)
   elif c==5:
       break
   else:
       print("invalid opr...")   