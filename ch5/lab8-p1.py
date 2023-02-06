number_of_students = eval(input("Enter number of students: "))

highest_name = None
highest_score = 0

for i in range(number_of_students):
    name = input("Enter student name: ")
    score = eval(input("Enter student score: "))

    if highest_score is None or highest_score < score:
        highest_name = name
        highest_score = score

print("\nTop student", highest_name + "'s score is", format(highest_score, ".1f"))


