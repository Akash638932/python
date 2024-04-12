print('''
      +add
      -subtract
      * multiply
      / divide
      ''')
num1=int(input("Enter the number1:-"))
num2=int(input("Enter the number2:-"))
opr=input("Enter the opr")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2) 
elif opr=="*":
    print(num1*num2) 
elif opr=="/":
    print(num1/num2)  
else:
    print("invaid opr...") 
    
#if khali used karane par    
    
num1=int(input("Enter the number1:-"))
num2=int(input("Enter the number2:-"))
opr=input("Enter the opr")
if opr=="+":
    print(num1+num2)
if opr=="-":
    print(num1-num2) 
if opr=="*":
    print(num1*num2) 
if opr=="/":
    print(num1/num2)  
if opr!="+"and opr!="-"and opr!="*"and opr!="/":
    print("invaid opr...") 