year = eval(input("Enter a year: "))

i = year % 12   # 0 ... 11
if i == 0:
    print("monkey")
elif i == 1:
    print("rooster")
elif i == 2:
    print("dog")
elif i == 3:
    print("pig")
elif i == 4:
    print("rat")
elif i == 5:
    print("ox")
elif i == 6:
    print("tiger")
elif i == 7:
    print("rabbit")
elif i == 8:
    print("dragon")
elif i == 9:
    print("snake")
elif i == 10:
    print("horse")
elif i == 11:
    print("sheep")
