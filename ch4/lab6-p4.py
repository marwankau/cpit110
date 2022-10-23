import random

# 0 scissor
# 1 rock
# 2 paper

computer_choice = random.randint(0, 2)
user_choice = eval(input("scissor (0), rock (1), paper (2): "))

if computer_choice == 0:
    if user_choice == 0:
        print("The computer is scissor. You are also scissor. It is a draw.")
    elif user_choice == 1:
        print("The computer is scissor. You are rock. You won.")
    else:
        print("The computer is scissor. You are paper. You lost.")
elif computer_choice == 1:
    if user_choice == 0:
        print("The computer is rock. You are also scissor. You lost.")
    elif user_choice == 1:
        print("The computer is rock. You are rock. It is a draw.")
    else:
        print("The computer is rock. You are paper. You won.")
else:  # computer is 2
    if user_choice == 0:
        print("The computer is paper. You are scissor. You won.")
    elif user_choice == 1:
        print("The computer is paper. You are rock. You lost.")
    else:
        print("The computer is paper. You are paper. It is draw.")



