
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

from app.utils.file_manager import ReportWriter


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


with ReportWriter("reports/You.txt") as report:
    report.write("CAMPUSHUB ERP - STUDENT REPORT\n")
    report.write("==============================\n")

    for item in student_report():
        report.write(str(item.to_dict()) + "\n")


with ReportWriter("reports/faculty.txt") as report:
    report.write("CAMPUSHUB ERP - FACULTY REPORT\n")
    report.write("==============================\n")

    for item in faculty_report():
        report.write(str(item.to_dict()) + "\n")


with ReportWriter("reports/courses.txt") as report:
    report.write("CAMPUSHUB ERP - COURSE REPORT\n")
    report.write("============================\n")

    for item in course_report():
        report.write(str(item.to_dict()) + "\n")


print("\nAll reports generated successfully!")
print("Check the reports folder.")
