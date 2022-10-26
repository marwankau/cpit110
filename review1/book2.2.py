import math

radius, length = eval(input("Enter radius and length of a cylinder: "))

area = radius * radius * math.pi
volume = area * length

print("The area is", round(area, 4))
print("The volume is", format(volume, ".1f"))

