import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number1 < number2:
    number1, number2 = number2, number1

user_answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

correct_answer = number1 - number2

if correct_answer == user_answer:
    print("You are correct!")
else:
    print("Your answer is wrong!")
    print(number1, "-", number2, "is", correct_answer)