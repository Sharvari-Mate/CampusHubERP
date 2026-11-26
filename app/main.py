
from flask import Flask
import asyncio

from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course

from app.services.async_service import (
    load_all_data,
    generate_all_reports
)

from app.api.You import student_api
from app.api.faculty import faculty_api
from app.api.courses import course_api
from app.api.enrollments import enrollment_api

app = Flask(__name__)

app.register_blueprint(student_api)
app.register_blueprint(faculty_api)
app.register_blueprint(course_api)
app.register_blueprint(enrollment_api)

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


print("\n========== CAMPUSHUB ERP ==========")

print("\n--- STUDENT INFORMATION ---")
student.display_details()

print("\n--- FACULTY INFORMATION ---")
faculty.display_details()

print("\n--- COURSE INFORMATION ---")
course.display_details()

print("\n========== ALL RECORDS ==========")

print("Student:", student.to_dict())
print("Faculty:", faculty.to_dict())
print("Course:", course.to_dict())

print("\nCAMPUSHUB ERP RUN COMPLETED")


async def async_main():
    await load_all_data()
    print("All data loaded successfully.")

    await generate_all_reports()

    print("CampusHub ERP completed successfully.")


if __name__ == "__main__":
    asyncio.run(async_main())

    print("\nStarting CampusHub ERP API...")
    app.run(debug=True)
