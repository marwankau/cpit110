import random

num1 = random.randint(0, 10)
num2 = random.randint(0, 10)
correct_answer = num1 + num2

student_answer = eval(input("find " + str(num1) + " + " + str(num2) + " = "))

if student_answer == correct_answer:
    print("You are correct, congrats")
else:
    print("Your answer is wrong")
    print("correct answer is", num1, "+", num2, "=", correct_answer)
