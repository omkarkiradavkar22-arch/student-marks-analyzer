import csv
import os

name = input("Enter student full name: ")
subjects = ["Python", "Database", "Maths", "English", "Computer" ]
marks = []
for subject in subjects:
    mark = float (input(f"Enter marks for {subjects}: "))
    marks.append(mark)
total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "B+"
elif average >= 50:
    grade = "D"
else:
    grade = "F"
result = "PASS" if average >= 40 else "FAIL"
print(f"Student Name :  {name}")
print(f"Total Marks  :  {total}")
print(f"Average      :  {average:.2f}")
print(f"Grade        :  {grade}")
print(f"Result       :  {result}")

file_name = "student_results.csv"
file_exists = os.path.exists(file_name)

with open(file_name , "a", newline ="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Student name"
            "Total Marks"
            "Average"
            "Grade"
            "Results"
        ])

    writer.writerow([
        name,
        total,
        round(average,2),
        grade,
        result
    ])
    
print("\nResult has been saved to student_result.csv")
