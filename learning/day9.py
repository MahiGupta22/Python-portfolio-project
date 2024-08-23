student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}
names=[]
names=student_scores.keys()
for i in names:
    if 100>=student_scores.get(i)>=91:
        Grade="Outstanding"
    elif 90>=student_scores.get(i)>=81:
        Grade="Exceeds Expectations"
    elif 80>=student_scores.get(i)>=71:
        Grade="Acceptable"
    elif 70>=student_scores.get(i)>=0:
        Grade="Fail"
    else:
        print("invalid")
    student_grades[i]=Grade
print(student_grades)
