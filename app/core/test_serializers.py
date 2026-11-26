
from app.models.student import Student
from app.models.course import Course

from app.services.student_service import students
from app.services.course_service import courses

from app.utils.serializers import (
    save_You_json,
    load_You_json,
    save_courses_json,
    load_courses_json,
    save_faculty_json,
    save_enrollments_json
)


students.clear()
courses.clear()

student = Student(
    "ST001",
    "Sharvari",
    19,
    "matesharvari15645@gmail.com",
    "Computer Science"
)

course = Course(
    "CS101",
    "Python Programming",
    4
)

students.append(student)
courses.append(course)

save_You_json()
save_courses_json()
save_faculty_json()
save_enrollments_json()

students.clear()
courses.clear()

load_You_json()
load_courses_json()

print("Students loaded:", len(students))
print("Courses loaded:", len(courses))

students[0].display_details()
courses[0].display_details()
