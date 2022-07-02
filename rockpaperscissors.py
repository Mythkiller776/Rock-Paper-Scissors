from random import randint

t = ["rock","paper","scissors"]
computer = t[randint(0,2)]

player = False
while player == False:
    player = input("rock,paper,scissors")
    if player == computer:
        print("tie")
    elif player== "rock":
        if computer == "paper":
            print("You Loose !",computer,"covers", player)
        else:
            print("You Win !",player,"smashes",computer)


    elif player == "paper":
        if computer == "rock":
            print("You Win !",player,"covers",computer)
        else:
            print("You Loose!",computer,"smashes",player)
        
    elif player == "scissors":
        if computer == "rock":
            print("You Loose!",computer,"smashes",player)
        else:
            print("You Win!",player,"cuts",computer)
        
    player = False
    computer = t[randint(0,2)]

