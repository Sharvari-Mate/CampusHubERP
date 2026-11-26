
from app.models.student import Student
from app.models.course import Course

from app.services.enrollment_service import (
    enroll_student,
    remove_enrollment,
    list_enrollments
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

course1 = Course(
    course_code="CS101",
    course_name="Python Programming",
    credits=4
)

course2 = Course(
    course_code="CS102",
    course_name="Database Management",
    credits=3
)


print("\n--- ENROLL STUDENTS ---")

enroll_student(student1, course1)
enroll_student(student2, course2)


print("\n--- LIST ENROLLMENTS ---")

for enrollment in list_enrollments():
    print(
        enrollment["student"].name,
        "->",
        enrollment["course"].course_name
    )


print("\n--- REMOVE ENROLLMENT ---")

remove_enrollment("ST002", "CS102")


print("\n--- FINAL ENROLLMENTS ---")

for enrollment in list_enrollments():
    print(
        enrollment["student"].name,
        "->",
        enrollment["course"].course_name
    )
