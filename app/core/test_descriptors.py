
from app.core.descriptors import Name, Email, Age


class TestStudent:
    name = Name()
    email = Email()
    age = Age()


student = TestStudent()

student.name = "Sharvari"
student.email = "matesharvari15645@gmail.com"
student.age = 19

print("VALID DATA:", student.name, student.email, student.age)

try:
    student.name = ""
except ValueError as e:
    print("NAME TEST PASSED:", e)

try:
    student.email = "invalidemail"
except ValueError as e:
    print("EMAIL TEST PASSED:", e)

try:
    student.age = 12
except ValueError as e:
    print("AGE TEST PASSED:", e)

print("ALL TESTS COMPLETED")
