import random

computer = random.randint(0, 2)

user = eval(input("scissor (0), rock (1), paper (2): "))

if computer == 0:
    if user == 0:
        print("Draw!, Both of you and computer chose scissor")
    elif user == 1:
        print("You win, computer choose scissor and you are rock")
    elif user == 2:
        print("Computer win, computer choose scissor and you are paper")
elif computer == 1:
    if user == 0:
        print("You lose, Computer win!, Computer is rock and you are scissor")
    elif user == 1:
        print("Draw, both you and computer choose rock")
    elif user == 2:
        print("You win, computer choose rock and you are paper")
elif computer == 2:
    if user == 0:
        print("You win, Computer is paper and you are scissor")
    elif user == 1:
        print("You lose, Computer win, computer choose paper and you are rock")
    elif user == 2:
        print("Draw!, both you and computer choose paper")