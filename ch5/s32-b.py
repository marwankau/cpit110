import random

number = random.randint(0, 100)

guess = 120

while guess != number:
    guess = eval(input("Enter your guess: "))
    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")


print("Yes!, the number is", number)

