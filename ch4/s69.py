year = eval(input("Enter a year: "))
zodiac = year % 12

if zodiac == 0:
    print("monkey")
elif zodiac == 1:
    print("rooster")
elif zodiac == 2:
    print("dog")
elif zodiac == 3:
    print("pig")
elif zodiac == 4:
    print("rat")
elif zodiac == 5:
    print("ox")
elif zodiac == 6:
    print("tiger")
elif zodiac == 7:
    print("rabbit")
elif zodiac == 8:
    print("dragon")
elif zodiac == 9:
    print("snake")
elif zodiac == 10:
    print("horse")
else:
    print("sheep")

