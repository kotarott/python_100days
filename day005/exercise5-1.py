# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# print(sum(student_heights) / len(student_heights))

sum_of_heights = 0
number_of_students = 0
for height in student_heights:
    sum_of_heights += height
    number_of_students += 1

print(sum_of_heights/number_of_students)