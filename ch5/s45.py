import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

solution = num1 - num2

userAnswer = eval(input("What is " + str(num1) + " - " + str(num2) + "? "))

if userAnswer == solution:
    print("You are correct!")
else:
    print("Your answer is wrong.")
    print(num1, "-", num2, "is", solution)

