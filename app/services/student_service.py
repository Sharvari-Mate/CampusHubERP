students = []


def add_student(student):
    students.append(student)
    print("Student added successfully")


def remove_student(student_id):
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("Student removed successfully")
            return

    print("Student not found")


def update_student(student_id, updated_student):
    for index, student in enumerate(students):
        if student.student_id == student_id:
            students[index] = updated_student
            print("Student updated successfully")
            return

    print("Student not found")


def list_students():
    return students


def list_You():
    return students
