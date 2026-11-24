from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course


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
