weight_in_pounds = eval(input("Enter weight in pounds: "))
height_in_inches = eval(input("Enter height in inches: "))

weight = weight_in_pounds * 0.45359237  # converted to KG
height = height_in_inches * 0.0254      # converted to meters

bmi = round(weight / (height ** 2), 2)

print("BMI is", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25.0:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")

