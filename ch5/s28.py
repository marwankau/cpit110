import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

correct_answer = num1 - num2

your_answer = eval(input("What is " + str(num1) + " - " + str(num2) + " ? "))

while your_answer != correct_answer:
    your_answer = eval(input("wrong answer. Try again. What is " + str(num1) + " - " + str(num2) + " ? "))

print("You got it!")
