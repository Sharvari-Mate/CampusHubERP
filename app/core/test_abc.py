
from app.core.abc_interfaces import Person


class Student(Person):

    def display_details(self):
        print("Name: Sharvari")
        print("Email: matesharvari15645@gmail.com")
        print("Age: 19")

    def to_dict(self):
        return {
            "name": "Sharvari",
            "email": "matesharvari15645@gmail.com",
            "age": 19
        }


student = Student()

student.display_details()

print("Student Dictionary:", student.to_dict())

print("ABC TEST COMPLETED")

