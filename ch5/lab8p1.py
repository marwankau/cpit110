numberOfStudents = eval(input("Enter number of students: "))

if numberOfStudents > 0:
    topName = input("Enter student name: ")
    topScore = eval(input("Enter a student score: "))

    for i in range(numberOfStudents - 1):
        name = input("Enter student name: ")
        score = eval(input("Enter a student score: "))

        if score > topScore:
            topName = name
            topScore = score

    print("Top student", topName + "'s score is", format(topScore, ".1f"))


