seconds = eval(input("Enter amount of time in seconds: "))

minutes = seconds // 60
remaining_seconds = seconds % 60

print(seconds, "seconds is", minutes, "minutes and", remaining_seconds, "seconds")

