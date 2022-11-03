numberOfStudents = eval(input("Enter number of students: "))

if numberOfStudents > 0:
    topName = None
    topScore = None
    secondName = None
    secondScore = None

    for i in range(numberOfStudents):
        name = input("Enter student name: ")
        score = eval(input("Enter a student score: "))

        if topName is None or score > topScore:
            secondName = topName
            secondScore = topScore
            topName = name
            topScore = score
        elif secondName is None or score > secondScore:
            secondName = name
            secondScore = score

    print("Top student", topName + "'s score is", format(topScore, ".1f"))
    print("Second student", secondName + "'s score is", format(secondScore, ".1f"))


