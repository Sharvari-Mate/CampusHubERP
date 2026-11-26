
from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course

from app.services.student_service import students
from app.services.faculty_service import faculty_members
from app.services.course_service import courses
from app.services.enrollment_service import enrollments

from app.utils.serializers import export_data, import_data


students.clear()
faculty_members.clear()
courses.clear()
enrollments.clear()

student = Student(
    "ST001",
    "Sharvari",
    19,
    "matesharvari15645@gmail.com",
    "Computer Science"
)

faculty = Faculty(
    "FC001",
    "Rahul",
    35,
    "rahul@example.com",
    "Computer Science"
)

course = Course(
    "CS101",
    "Python Programming",
    4
)

students.append(student)
faculty_members.append(faculty)
courses.append(course)

enrollments.append({
    "student": student,
    "course": course
})

export_data()

students.clear()
faculty_members.clear()
courses.clear()
enrollments.clear()

import_data()

print("Students restored:", len(students))
print("Faculty restored:", len(faculty_members))
print("Courses restored:", len(courses))
print("Enrollments restored:", len(enrollments))
