grades = [4,5,3,5,4,2,5]

minimum = grades [0]
maximum = grades [0]
total = 0

for grade in grades:
    if grade < minimum:
        minimum = grade
    total = total + grade
average = total/len (grades)

print ("Минимальная оценка:",minimum)
print ("Максимальная оценка:",maximum)
print ("Средний балл:",average)
