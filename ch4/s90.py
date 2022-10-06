weight = eval(input("Enter weight in pounds: "))
height = eval(input("Enter height in inches: "))

POUND_TO_KG = 0.45359237
INCH_TO_M = 0.0254

weight_in_kg = weight * POUND_TO_KG
height_in_m = height * INCH_TO_M

bmi = weight_in_kg / (height_in_m ** 2)

print("BMI is", format(bmi, ".2f"))

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")


