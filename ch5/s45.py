import time
import random

i = 0
number_of_correct = 0
start_time = time.time()

while i < 5:
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    if num1 < num2:
        num1, num2 = num2, num1

    answer = eval(input("What is " + str(num1) + " - " + str(num2) + " ? "))
    correct_answer = num1 - num2
    
    if answer == correct_answer:
        print("You are correct!")
        number_of_correct += 1
    else:
        print("Your answer is wrong\n", num1, "-", num2, "is", correct_answer)

    i = i + 1
    print()

end_time = time.time()
print("Correct count is", number_of_correct, "out of 5")
print("Test time is", int(end_time - start_time), "seconds")
