import random

number = random.randint(10, 99)

guss = eval(input("Enter your picked number: "))

number1 = number % 10
number2 = number // 10

guss1 = guss % 10
guss2 = guss // 10

print("Winning number is", number)

if number1 == guss1 and number2 == guss2:  # guss == number
    print("You got 10,000")
elif number1 == guss2 and number2 == guss1:
    print("You got 3,000")
elif number1 == guss1 or number1 == guss2 or number2 == guss1 or number2 == guss2:
    print("You got 1,000")
else:
    print("You lost")