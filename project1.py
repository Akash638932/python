import random
l=["rock","scissor","paper"]
'''
rock vs paper-> paper wins
rock vs scissor-> wins
paper vs scissor->scissor wins.

'''

while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game start''''''''''''
1 yes
2 no|Exit

       '''))
    if uc==1:
         for i in range(1,6):
            userInput=int(input('''
 1 Rock
 2 Scissor
 3 Pepar                               
'''))
            if userInput==1:
               uchoice="rock"
            elif userInput==2:
             uchoice="scissor"
            elif userInput==3:
               uchoice="paper"
            cchoice=random.choice(l)
            if cchoice==uchoice:
              print("computer value",cchoice)
              print("user value ",uchoice)
              print("game Draw")
              ucount=ucount+1
              ccount=ccount+1
            elif(uchoice=="rock" and cchoice=="scissor") or (uchoice
               =="paper" and cchoice=="rock") or (uchoice=="scissor"
               and cchoice=="paper"):
               print("computer value",cchoice)
               print("user value ",uchoice)
               print("you win")  
               ucount=ucount+1
            else:
               print("computer value",cchoice)
               print("user value ",uchoice)
               print("computer win")  
               ucount=ucount+1
               if ucount==ccount:
                  print("final game drow...")
                  print("user score",ucount)
                  print("computer score",ccount)
               elif ucount>ccount:
                  print("final you win the game....")
                  print("user score",ccount)
                  print("computer score",ccount)
         else:
                  print("final computer win the game.....")
                  print("user score",ucount)
                  print("computer score",ccount)
    else:
           break