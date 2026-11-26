
from app.utils.decorators import log_decorator, time_decorator

from app.utils.logger import (
    log_student_added,
    log_student_updated,
    log_student_deleted,
    log_error
)

from database.repository import (
    add_student as repository_add_student,
    delete_student as repository_delete_student,
    update_student as repository_update_student,
    get_all_students
)


students = get_all_students()


def refresh_students():
    students.clear()
    students.extend(get_all_students())


@log_decorator
@time_decorator
def add_student(student):
    try:
        repository_add_student(student)
        refresh_students()

        log_student_added(student.student_id)

        print("Student added successfully")

    except Exception as error:
        log_error(f"Error adding student: {error}")
        raise


@log_decorator
@time_decorator
def remove_student(student_id):
    try:
        removed = repository_delete_student(student_id)

        if removed:
            refresh_students()

            log_student_deleted(student_id)

            print("Student removed successfully")
        else:
            print("Student not found")

    except Exception as error:
        log_error(f"Error deleting student: {error}")
        raise


@log_decorator
@time_decorator
def update_student(student_id, updated_student):
    try:
        updated = repository_update_student(
            student_id,
            name=updated_student.name,
            age=updated_student.age,
            email=updated_student.email,
            department=updated_student.department
        )

        if updated:
            refresh_students()

            log_student_updated(student_id)

            print("Student updated successfully")
        else:
            print("Student not found")

    except Exception as error:
        log_error(f"Error updating student: {error}")
        raise


@log_decorator
@time_decorator
def list_students():
    refresh_students()
    return get_all_students()


@log_decorator
@time_decorator
def list_You():
    refresh_students()
    return get_all_students()


@log_decorator
@time_decorator
def list_student_names_uppercase():
    student_records = get_all_students()
    return list(map(lambda student: student.name.upper(), student_records))


@log_decorator
@time_decorator
def filter_students_by_department(department):
    student_records = get_all_students()

    return list(
        filter(
            lambda student: student.department == department,
            student_records
        )
    )


@log_decorator
@time_decorator
def sort_students_by_name():
    student_records = get_all_students()
    return sorted(student_records, key=lambda student: student.name)
