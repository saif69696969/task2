# ==========================================
# TASK 2: Decision Making & Conditions
# ==========================================

# Question 1: Overtime Pay Calculator
print("--- Question 1: Overtime Pay ---")
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    total_pay = hours * rate
else:
    total_pay = (40 * rate) + ((hours - 40) * rate * 1.5)
print(f"Total Pay: ${total_pay:.2f}")

# Question 2: Advanced Student Marksheet
print("\n--- Question 2: Student Marksheet ---")
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

marks = []
has_failed_subject = False
print("Enter marks for 5 subjects (out of 100):")
for i in range(1, 6):
    score = float(input(f"Subject {i}: "))
    marks.append(score)
    if score < 40:
        has_failed_subject = True

total_marks = sum(marks)
percentage = (total_marks / 500) * 100

if has_failed_subject or percentage < 40:
    result = "FAIL"
else:
    result = "PASS"

if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("\n" + "=" * 35)
print("         STUDENT MARKSHEET         ")
print("=" * 35)
print(f"Name       : {name}")
print(f"Roll No.   : {roll_no}")
print("-" * 35)
for i, m in enumerate(marks, start=1):
    print(f"Subject {i}  : {m:.2f} / 100")
print("-" * 35)
print(f"Total Marks: {total_marks:.2f} / 500")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
print(f"Result     : {result}")
print("=" * 35)