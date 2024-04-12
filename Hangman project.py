import random
import time
print("welcome to hangman games")
name=input("Enter your name:-")
print("Hello" + name +"! Best of luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game 
    words_to_guess=["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    random.choice(words_to_guess)
    length=len(word)
    count=0
    display='_'*length 
    already_guessed=[]
    play_game=" "
def play_loop():
    global play_game
    play_game=input("Do You again? y=yes,n = no\n")
    while play_game not in["y","n","Y","N"]:
        play_game=("Do you want to play again? y=yes,n=no\n")
        if play_game=="y":
            main()
        elif play_game=="n":
            print("Thanks For playing! We expect you back again!")
            exit()
def hungman():
        global count
        global display
        global word
        global already_guessed
        global play_game
        limit=5
        guess=input("This is the hangman Word:"+ display +"your guess:/n") 
        guress=guess.strip()