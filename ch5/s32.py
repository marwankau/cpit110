import random

target = random.randint(0, 100)

guess = 101

while guess != target:
    guess = eval(input("Enter your guess: "))

    if guess > target:
        print("Your guess is too high")
    elif guess < target:
        print("Your guess is too low")
    else:
        print("Yes, the number is", target)