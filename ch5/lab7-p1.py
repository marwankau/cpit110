positive = 0
negative = 0
total = 0
userInput = 8

while userInput != 0:
    userInput = eval(input("Enter an integer, the input ends if it is 0: "))
    total = total + userInput
    if userInput > 0:
        positive = positive + 1
    elif userInput < 0:
        negative = negative + 1

count = positive + negative
if count > 0:
    print("The number of positives is", positive)
    print("The number of negatives is", negative)
    print("Total is", total)
    average = total / count
    print("Average is", average)
else:
    print("No numbers are entered except 0")

