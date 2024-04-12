l=[]
while True:
    c=int(input('''
                1.push Elements
                2.pop Elements
                3.front Elements
                4.last Elements
                5.display queue
                6.Exit
                '''))
    if c==1:
        n=input("Enter the value:-")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Enter queue")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l)==0:
           print("Empty queue")
        else:
           print("first queue value:-",l[0])
    elif c==4:
        if len(l)==0:
            print("Empty queue")
        else:
            print("last queue value :-",l[-1])   
    elif c==5:
        print("display queue",1)
    elif c==6:
        break;
    else:
        print("invalid opr...")