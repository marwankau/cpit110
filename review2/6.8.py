def celsiusToFahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit


def fahrenheitToCelsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)

    return celsius


choice = eval(input("(1) Convert celsius to fahrenheit, (2) Convert fahrenheit to celsius: "))

if choice == 1:
    celsius = eval(input("Enter celsius value: "))
    print(celsius, "celsius equals", celsiusToFahrenheit(celsius), "fahrenheit")
elif choice == 2:
    fahrenheit = eval(input("Enter fahrenheit value: "))
    print(fahrenheit, "fahrenheit equals", fahrenheitToCelsius(fahrenheit), "celsius")
