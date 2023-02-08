num_of_courses = eval(input("Enter the number of courses: "))

total_scores = 0

for i in range(num_of_courses):
    score = eval(input("Enter the score of course: "))
    total_scores += score

average = (total_scores / num_of_courses) * 1.10

print("The score after bonus for all courses is", average)

