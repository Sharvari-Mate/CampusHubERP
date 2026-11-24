
from app.models.course import Course

from app.services.course_service import (
    add_course,
    remove_course,
    update_course,
    list_courses
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


print("\n--- ADD COURSES ---")
add_course(course1)
add_course(course2)


print("\n--- LIST COURSES ---")
for course in list_courses():
    course.display_details()


print("\n--- UPDATE COURSE ---")
updated_course = Course(
    course_code="CS101",
    course_name="Advanced Python Programming",
    credits=5
)

update_course("CS101", updated_course)


print("\n--- LIST AFTER UPDATE ---")
for course in list_courses():
    course.display_details()


print("\n--- REMOVE COURSE ---")
remove_course("CS102")


print("\n--- FINAL COURSE LIST ---")
for course in list_courses():
    course.display_details()
