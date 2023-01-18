import random

number = random.randint(0, 100)

guess = eval(input("Enter your guess: "))

while guess != number:
    if guess < number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

    guess = eval(input("Enter your guess: "))

print("Yes!, the number is", number)

