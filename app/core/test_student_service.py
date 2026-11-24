from app.models.student import Student

from app.services.student_service import (
    add_student,
    remove_student,
    update_student,
    list_students
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


print("\n--- ADD STUDENTS ---")
add_student(student1)
add_student(student2)


print("\n--- LIST STUDENTS ---")
for student in list_students():
    student.display_details()


print("\n--- UPDATE STUDENT ---")
updated_student = Student(
    student_id="ST001",
    name="Sharvari Mate",
    age=19,
    email="matesharvari15645@gmail.com",
    department="Computer Science"
)

update_student("ST001", updated_student)


print("\n--- LIST AFTER UPDATE ---")
for student in list_students():
    student.display_details()


print("\n--- REMOVE STUDENT ---")
remove_student("ST002")


print("\n--- FINAL STUDENT LIST ---")
for student in list_students():
    student.display_details()
