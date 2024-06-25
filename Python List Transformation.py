#Task 1: Given the list of grades
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.reverse()
print(grades)

#Task 2: Calculate the average grade and print it.
#grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
#no need to redeclare the list since we already had it above :D
total_sum = sum(grades)
num_grades = len(grades)
average_grade = total_sum / num_grades
print("Average grade:", average_grade)