import random
import time

count = 0
score = 0
start = time.time()
while count < 5:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    solution = num1 - num2

    userAnswer = eval(input("What is " + str(num1) + " - " + str(num2) + "? "))

    if userAnswer == solution:
        score = score + 1
        print("You are correct!")
    else:
        print("Your answer is wrong.")
        print(num1, "-", num2, "is", solution)

    print()
    count += 1

print("Correct count is", score, "out of 5")
end = time.time()

duration = end - start
print("Test time is", int(duration), "seconds")
