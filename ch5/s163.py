sum = 0
number = 0

while number < 20:
    number = number + 1
    sum = sum + number

    if sum >= 100:
        break

print("sum =", sum)
print("number =", number)