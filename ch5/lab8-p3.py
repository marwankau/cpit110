numOfStudent = eval(input("Enter number of students: "))

topStudent = ""
topScore = -1

secondName = ""
secondScore = -1

for i in range(numOfStudent):
    name = input("Enter student name: ")
    score = eval(input("Enter student score: "))

    if topScore < score:
        secondName = topStudent
        secondScore = topScore
        topStudent = name
        topScore = score
    elif secondScore < score:
        secondName = name
        secondScore = score

print()
print("Top two students:")
print(topStudent + "'s score is", topScore)
print(secondName + "'s score is", secondScore)
