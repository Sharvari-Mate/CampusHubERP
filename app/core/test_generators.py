
from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course

from app.services.student_service import add_student
from app.services.faculty_service import add_faculty
from app.services.course_service import add_course

from app.utils.generators import (
    student_report,
    faculty_report,
    course_report
)


student = Student(
    student_id="ST001",
    name="Sharvari",
    age=19,
    email="matesharvari15645@gmail.com",
    department="Computer Science"
)

faculty = Faculty(
    faculty_id="FC001",
    name="Rahul Sharma",
    age=35,
    email="rahul@gmail.com",
    department="Computer Science"
)

course = Course(
    course_code="CS101",
    course_name="Python Programming",
    credits=4
)


add_student(student)
add_faculty(faculty)
add_course(course)


print("\n--- STUDENT GENERATOR ---")
for item in student_report():
    item.display_details()


print("\n--- FACULTY GENERATOR ---")
for item in faculty_report():
    item.display_details()


print("\n--- COURSE GENERATOR ---")
for item in course_report():
    item.display_details()
