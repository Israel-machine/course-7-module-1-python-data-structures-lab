# This module contains functions for filtering student data.
from student_data import students

def filter_students_by_major(student_list, major):
    filtered = [student for student in student_list if major in student]
    print(f"\n Tasks matching {major}: {filtered}")

filter_students_by_major(students, "Mathematics")
"""
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
"""
