student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

# write your code below this code
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score <= 70:
        grade = "Fail"
    elif score > 70 and score <= 80:
        grade = "Acceptable"
    elif score >80 and score <= 90:
        grade = "Exceeds Expectations"
    else:
        grade = "Outstanding"
    student_grades[student] = grade

#
print(student_grades)