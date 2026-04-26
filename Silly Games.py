import random
choices=["s","w","g"]
names ={"s":"snake","w":"water","g":"gun"}

score={"player":0,"computer":0,"draw":0}

print("Welcome to Silly Games!")
print("==THE GAME IS SNAKE , WATER ,GUN==")
print("type 'q' to quit\n")

while True:
    player=input("Enter your choice:").lower()
    if player == "q":
        print("Thank you for playing")
        break
    if player not in choices:
        print("Please enter valid choice")
        continue
    computer=random.choice(choices)

    print(f"Computer chose: {names[computer]}")
    print(f"you chose", {names[player]})

    if player == computer:
        print("Draw")
        score["draw"]+=1
    elif player == "g" and computer == "s":
        print("You win")
        score["player"]+=1
    elif player == "s" and computer == "w":
        print("You win")
        score["player"]+=1
    elif player == "w" and computer == "g":
        print("You loose")
        score["computer"]+=1
    elif player == "g" and computer == "w":
        print("You lose")
        score["computer"]+=1
    elif player == "s" and computer == "g":
        print("You loose")
        score["computer"]+=1
    elif player == "w" and computer == "s":
        print("You win")
        score["player"]+=1
    else:
        print("Its draw")
    score["draw"]+=1
    break

print("thanks for playing:-)")


