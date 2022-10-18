import random

ones = random.randint(0, 9)
tenth = random.randint(1, 9)

winning_number = ones + tenth * 10
reversed_number = ones * 10 + tenth


user_number = eval(input("Enter your lottery pick (two digits): "))

user_ones = user_number % 10    # 45 -> 5
user_tenth = user_number // 10  # 45 -> 4

print("The lottery number is", winning_number)
if user_number == winning_number:
    print("You win! $10,000")
elif user_number == reversed_number:
    print("You win! $3,000")
elif user_ones == ones or user_ones == tenth or user_tenth == ones or user_tenth == tenth:
    print("You win! $1,000")
else:
    print("Sorry, No match")


