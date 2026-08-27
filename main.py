import csv
import os

name = input("Enter student full name: ")

subjects = ["Python", "Database", "Maths", "English", "Computer"]
credits = [4, 4, 3, 3, 4]

grade_points = []

for i, subject in enumerate(subjects):
    point = float(input(f"Enter grade point for {subject} (0-10): "))
    grade_points.append(point)

total_credit_points = 0
total_credits = sum(credits)

for i in range(len(subjects)):
    total_credit_points += grade_points[i] * credits[i]

cgpa = total_credit_points / total_credits

print("\n----- STUDENT RESULT -----")
print(f"Student Name : {name}")
print(f"CGPA         : {cgpa:.2f}")

if cgpa >= 9:
    result = "Excellent"
elif cgpa >= 8:
    result = "Very Good"
elif cgpa >= 7:
    result = "Good"
elif cgpa >= 6:
    result = "Average"
elif cgpa >= 5:
    result = "Pass"
else:
    result = "Fail"

print(f"Result       : {result}")

file_name = "student_cgpa.csv"
file_exists = os.path.exists(file_name)

with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Student Name",
            "CGPA",
            "Result"
        ])

    writer.writerow([
        name,
        round(cgpa, 2),
        result
    ])

print("\nCGPA result has been saved to student_cgpa.csv")