# This module contains functions to process student data.
from student_data import students

def format_student_data(student):
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """

def display_students(student_list):
    for s in student_list:
        print(format_student_data(s))

display_students(students)
"""
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    
    """