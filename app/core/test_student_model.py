from app.models.student import Student


student = Student(
    student_id="ST001",
    name="Sharvari",
    age=19,
    email="matesharvari15645@gmail.com",
    department="Computer Science"
)

print("STUDENT DETAILS")
student.display_details()

print("\nSTUDENT DICTIONARY")
print(student.to_dict())

print("\nCREATED AT:", student.created_at())
print("UPDATED AT:", student.updated_at())

print("\nSTUDENT MODEL TEST COMPLETED")
