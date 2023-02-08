wp1, wp2, wp3 = eval(input("Enter weight of three passengers in an elevator: "))
current_load = wp1 + wp2 + wp3

print("Current load =", current_load, "kilograms")

MAX_LOAD = 201

if current_load > MAX_LOAD:
    print("Overload")
elif current_load == MAX_LOAD:
    print("Max load")
else:
    print("Normal load")
