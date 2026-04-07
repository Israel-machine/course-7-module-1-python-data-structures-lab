# This module contains functions to lazily generate student data.
from student_data import students

def student_generator(student_list, major):
    return (student for student in student_list if student[2] == major)

math_gen = student_generator(students, "Mathematics")

print(next(math_gen))  
print(next(math_gen))  

"""
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    pass
    """
