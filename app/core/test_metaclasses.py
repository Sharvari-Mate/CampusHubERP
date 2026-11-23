from app.core.metaclasses import ModelMeta


class Student(metaclass=ModelMeta):
    pass


student = Student()

print("Created At:", student.created_at())
print("Updated At:", student.updated_at())

print("METACLASS TEST COMPLETED")
