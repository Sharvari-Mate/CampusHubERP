
from app.utils.decorators import log_decorator, time_decorator


students = []


@log_decorator
@time_decorator
def add_student(student):
    students.append(student)
    print("Student added successfully")


@log_decorator
@time_decorator
def remove_student(student_id):
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("Student removed successfully")
            return

    print("Student not found")


@log_decorator
@time_decorator
def update_student(student_id, updated_student):
    for index, student in enumerate(students):
        if student.student_id == student_id:
            students[index] = updated_student
            print("Student updated successfully")
            return

    print("Student not found")


@log_decorator
@time_decorator
def list_students():
    return students


@log_decorator
@time_decorator
def list_You():
    return students
