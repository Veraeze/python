trial = [[25, 50, 75], [40, 50, 60], [75, 65, 80]]
total = 0
students = 0
mainv = 0
for i in enumerate(trial):
    average = sum(i) / len(i)
    total += sum(i)
    students += len(i)
    mainv = total / students
    print(average)
print(mainv)
