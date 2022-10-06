import random

num1 = random.randrange(0, 100)
num2 = random.randrange(0, 100)

result = num1 + num2

user_answer = eval(input("what is " + str(num1) + " + " + str(num2) + "? "))

isUserAnswerCorrect = user_answer == result

print(num1, "+", num2, "=", user_answer, "is", isUserAnswerCorrect)

if not isUserAnswerCorrect:
    print("The correct answer is", result)
