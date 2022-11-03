numberOfStudents = eval(input("Enter number of students: "))

if numberOfStudents > 0:
    topName = None
    topScore = None

    for i in range(numberOfStudents):
        name = input("Enter student name: ")
        score = eval(input("Enter a student score: "))

        if topName is None or score > topScore:
            topName = name
            topScore = score

    print("Top student", topName + "'s score is", format(topScore, ".1f"))


