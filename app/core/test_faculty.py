from app.models.faculty import Faculty

faculty = Faculty(
    faculty_id="F001",
    name="Rahul Sharma",
    age=35,
    email="rahul@gmail.com",
    department="Computer Science"
)

print("FACULTY DETAILS")
faculty.display_details()

print("\nFACULTY DICTIONARY")
print(faculty.to_dict())

print("\nFACULTY MODEL TEST COMPLETED")

