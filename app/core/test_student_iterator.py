
from app.models.student import Student
from app.services.student_service import add_student, students
from app.utils.iterators import StudentIterator


students.clear()


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


add_student(student1)
add_student(student2)
add_student(student3)


print("\n--- STUDENT ITERATOR ---")

iterator = StudentIterator(students)

for student in iterator:
    student.display_details()
    print("----------------------")


print("Student iteration completed")
