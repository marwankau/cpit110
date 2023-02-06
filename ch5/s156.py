tuition = 10000
future_tuition = 20000
rate = 7 / 100
year = 0
current_tuition = tuition

while current_tuition < future_tuition:
    current_tuition += current_tuition * rate
    year += 1

print("The tuition doubled in", year, 'years')
print("The tuition will be", "$" + format(current_tuition, ".2f"), "in", year, 'years')
