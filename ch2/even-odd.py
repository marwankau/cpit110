day = eval(input("Enter day number: "))
num = eval(input("After how many days: "))

future_day = (day + num) % 7

print("it will be ", future_day)
