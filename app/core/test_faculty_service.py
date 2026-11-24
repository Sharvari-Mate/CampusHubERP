from app.models.faculty import Faculty

from app.services.faculty_service import (
    add_faculty,
    remove_faculty,
    update_faculty,
    list_faculty
)


faculty1 = Faculty(
    faculty_id="FC001",
    name="Rahul Sharma",
    age=35,
    email="rahul@gmail.com",
    department="Computer Science"
)

faculty2 = Faculty(
    faculty_id="FC002",
    name="Priya Shah",
    age=30,
    email="priya@gmail.com",
    department="Information Technology"
)


print("\n--- ADD FACULTY ---")
add_faculty(faculty1)
add_faculty(faculty2)


print("\n--- LIST FACULTY ---")
for faculty in list_faculty():
    faculty.display_details()


print("\n--- UPDATE FACULTY ---")
updated_faculty = Faculty(
    faculty_id="FC001",
    name="Rahul Sharma",
    age=36,
    email="rahul@gmail.com",
    department="Computer Science"
)

update_faculty("FC001", updated_faculty)


print("\n--- LIST AFTER UPDATE ---")
for faculty in list_faculty():
    faculty.display_details()


print("\n--- REMOVE FACULTY ---")
remove_faculty("FC002")


print("\n--- FINAL FACULTY LIST ---")
for faculty in list_faculty():
    faculty.display_details()
