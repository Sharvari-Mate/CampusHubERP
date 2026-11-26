
from app.core.validators import (
    validate_email,
    validate_student_id,
    validate_faculty_id,
    validate_course_code
)


print("Email:", validate_email("matesharvari15645@gmail.com"))
print("Student ID:", validate_student_id("ST001"))
print("Faculty ID:", validate_faculty_id("FC001"))
print("Course Code:", validate_course_code("CS101"))

print("Invalid Email:", validate_email("sharvariemail.com"))
print("Invalid Student ID:", validate_student_id("ST1"))
print("Invalid Faculty ID:", validate_faculty_id("FC12"))
print("Invalid Course Code:", validate_course_code("CS1"))
