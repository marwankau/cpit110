tuition = 10000
increase_rate = 7 / 100
new_tuition = tuition
year = 0

while new_tuition < 20000:
    year += 1
    new_tuition += new_tuition * increase_rate


print("Tuition will be doubled in", year, "years")
print("Tuition will be $" + format(new_tuition, ".2f"), "in", year, "years")
