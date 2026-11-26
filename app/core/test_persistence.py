
from database.repository import (
    get_all_students,
    get_all_faculty,
    get_all_courses,
    get_enrollments
)


print("\n--- SAVED STUDENTS ---")
students = get_all_students()

for student in students:
    print(
        student.student_id,
        student.name,
        student.age,
        student.email,
        student.department
    )


print("\n--- SAVED FACULTY ---")
faculty_members = get_all_faculty()

for faculty in faculty_members:
    print(
        faculty.faculty_id,
        faculty.name,
        faculty.age,
        faculty.email,
        faculty.department
    )


print("\n--- SAVED COURSES ---")
courses = get_all_courses()

for course in courses:
    print(
        course.course_code,
        course.course_name,
        course.credits
    )


print("\n--- SAVED ENROLLMENTS ---")
enrollments = get_enrollments()

for enrollment in enrollments:
    print(
        enrollment.student_id,
        enrollment.course_code
    )


print("\n--- DATABASE COUNTS ---")
print("Students:", len(students))
print("Faculty:", len(faculty_members))
print("Courses:", len(courses))
print("Enrollments:", len(enrollments))

print("\nPERSISTENCE CHECK COMPLETED")
