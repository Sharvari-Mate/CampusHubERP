from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course

from database.repository import (
    get_all_students,
    get_all_faculty,
    get_all_courses,
    add_student,
    get_You,
    update_student,
    add_faculty,
    get_faculty,
    update_faculty,
    add_course,
    get_course,
    update_course,
    add_enrollment,
    get_enrollments
)


student = Student(
    "ST902",
    "Sharvari",
    19,
    "matesharvari15645@gmail.com",
    "Computer Science"
)

faculty = Faculty(
    "FC902",
    "Rahul",
    35,
    "rahul@example.com",
    "Computer Science"
)

course = Course(
    "CS902",
    "Database Systems",
    4
)

add_student(student)
add_faculty(faculty)
add_course(course)

print("Student:", get_You("ST902").name)
print("Faculty:", get_faculty("FC902").name)
print("Course:", get_course("CS902").course_name)

update_student("ST902", name="Sharvari Updated")
update_faculty("FC902", name="Rahul Updated")
update_course("CS902", course_name="Advanced Database Systems")

print("Updated Student:", get_You("ST902").name)
print("Updated Faculty:", get_faculty("FC902").name)
print("Updated Course:", get_course("CS902").course_name)

add_enrollment("ST902", "CS902")

print("Enrollments:", len(get_enrollments()))
print("Repository test completed.")

print("Total students:", len(get_all_students()))
print("Total faculty:", len(get_all_faculty()))
print("Total courses:", len(get_all_courses()))