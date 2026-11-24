
from app.models.student import Student

from app.services.student_service import (
    add_student,
    list_student_names_uppercase,
    filter_students_by_department,
    sort_students_by_name
)


student1 = Student(
    student_id="ST001",
    name="Sharvari",
    age=19,
    email="matesharvari15645@gmail.com",
    department="Computer Science"
)

student2 = Student(
    student_id="ST002",
    name="Aarav",
    age=20,
    email="aarav@gmail.com",
    department="Information Technology"
)

student3 = Student(
    student_id="ST003",
    name="Rahul",
    age=21,
    email="rahul@gmail.com",
    department="Computer Science"
)


print("\n--- ADD STUDENTS ---")
add_student(student1)
add_student(student2)
add_student(student3)


print("\n--- MAP: UPPERCASE NAMES ---")
print(list_student_names_uppercase())


print("\n--- FILTER: COMPUTER SCIENCE ---")
for student in filter_students_by_department("Computer Science"):
    student.display_details()


print("\n--- SORTED: STUDENTS BY NAME ---")
for student in sort_students_by_name():
    student.display_details()
