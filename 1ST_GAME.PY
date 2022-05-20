import random
print("****** WELCOME TO ROCK PAPER SCISSORS ******\n\tIT'S MY MY FIRST GAME :)\n\t YOU WILL ENJOY")
print("It's Computer's turn to choose")
a = random.randint(1,3)

if a == 1 :
    comp = "r"
elif a == 2 :
    comp = "p"
else :
        comp = "s"

player = input("It's Players turn to choose between Rock(r), Paper(p), Scissor(s): ")
def test(comp, player):
    if(comp == player):
        return None
    elif(comp == "r"):
        if(player == "p"):
            return True
        if(player == "s"):
            return False
    elif(comp == "p"):
        if(player == "s"):
            return True
        if(player == "r"):
            return False
    elif(comp == "s"):
        if(player == "r"):
            return True
        if(player == "p"):
            return False
result = test(comp, player)
if(result == None):
    print(f"Computer's choice was {comp} and your choice was {player}")
    print("It's a Tie!!!!....Please try again")

elif (result):
    print(f"Computrer's choice was {comp} and your choice was {player}")
    print(f"Congrats!! Player Won")
else :
    print(f"Computer's choice was {comp} and your choice was {player}")
    print("You Lose :( Better luck next time :)")
