positives = 0
negatives = 0
s = 0
num = -1

while num != 0:
    num = eval(input("Enter an integer (0 to stop): "))
    s += num
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1


count = positives + negatives
if count == 0:
    print("There are no entry")
else:
    print("Number of positives is", positives)
    print("Number of negatives is", negatives)
    print("Total is", s)

    average = s / count
    print("Average is", average)
