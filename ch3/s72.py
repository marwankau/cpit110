firstName = input("Enter your name: ")
age = eval(input("Enter your age: "))

print(format("Name", "15s"), format("Age", "4s"))
print(format(firstName, "15s"), format(age, "4d"))
