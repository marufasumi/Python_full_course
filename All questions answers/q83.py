"""
Q83. Subject Performance Analysis

Given a dictionary of marks for different subjects, loop over its values() to
calculate and print the total marks and the average mark obtained.
"""

marks = {
    "Math": 88,
    "Science": 76,
    "English": 91,
    "History": 65,
    "Computer": 95,
}

total_subjects = len(marks)
total_marks = 0

for mark in marks.values():
    total_marks += mark

print(f"Avg = {total_marks/total_subjects}")
