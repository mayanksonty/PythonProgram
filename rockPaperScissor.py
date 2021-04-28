# This Game is Rock Paper and Scissor in which you will get only 10 chances and who win more no of games 
# will won the match
# r = rock, s = scissor, p = paper
import random

li = ["r","s","p"]

computer = 0
player = 0
i = 0
while(i<=10):
    # using random module and using the choice method of it
    comp = random.choice(li)
    rps = input("Enter r = rock, p = paper and s = scissor")
    rps = rps.lower()

    # All Cases 
    if rps == "r" and comp == "s":
        print("You won!!!")
        player = player+1
    elif rps == "r" and comp == "p":
        print("You lose!!!")
        computer = computer+1
    elif rps == "r" and comp == "r":
        print("The game is draw")
    elif rps == "p" and comp == "r":
        print("You Won!!")
        player = player+1
    elif rps == "p" and comp == "s":
        print("you lose")
        computer = computer+1
    elif rps == "p" and comp == "p":
        print("the game is draw")
    elif rps == "s" and comp == "r":
        print("you lose")
        computer = computer+1
    elif rps == "s" and comp == "p":
        print("you won")
        player = player+1
    elif rps == "s" and comp == "s":
        print("the game is draw")
    i = i+1

print(f"player score is {player} and Computer score is {computer}")
if player > computer:
    print("Player won!!!!!")
elif computer > player:
    print("Computer Won!!!!")