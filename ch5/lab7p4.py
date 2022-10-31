num = eval(input("Enter a number: (0: to end entries) "))
max = num
count = 1

while num != 0:
    num = eval(input("Enter a number: (0: to end entries) "))

    if num > max:
        max = num
        count = 1
    elif num == max:
        count += 1

print("The largest number is", max)
print("The occurrence count of the largest number is", count)
