sum = 0
number = 0

while number < 20:
    number = number + 1

    if number == 10 or number == 11:
        continue

    print(number, end=" + ")
    sum = sum + number

print()
print("sum =", sum)
print("number =", number)
