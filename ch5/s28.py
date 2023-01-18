import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number1 < number2:
    number1, number2 = number2, number1

user_answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

correct_answer = number1 - number2

while correct_answer != user_answer:
    print("Your answer is wrong!")
    user_answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))


print("You are correct!")

