import random

num1 = random.randint(0, 10)
num2 = random.randint(0, 10)
correct_answer = num1 + num2

student_answer = eval(input("find " + str(num1) + " + " + str(num2) + " = "))

is_correct = (student_answer == correct_answer)
print(num1, "+", num2, "=", student_answer, "is", is_correct)
