
from app.utils.decorators import log_decorator, time_decorator

from app.utils.logger import (
    log_faculty_added,
    log_error
)

from database.repository import (
    add_faculty as db_add_faculty,
    delete_faculty as db_delete_faculty,
    update_faculty as db_update_faculty,
    get_faculty as db_get_faculty,
    get_all_faculty as db_get_all_faculty
)


@log_decorator
@time_decorator
def add_faculty(faculty):
    try:
        db_add_faculty(faculty)

        log_faculty_added(faculty.faculty_id)

        print("Faculty added successfully")

    except Exception as error:
        log_error(f"Error adding faculty: {error}")
        raise


@log_decorator
@time_decorator
def remove_faculty(faculty_id):
    result = db_delete_faculty(faculty_id)

    if result:
        print("Faculty removed successfully")
    else:
        print("Faculty not found")


@log_decorator
@time_decorator
def update_faculty(faculty_id, updated_faculty):
    result = db_update_faculty(
        faculty_id,
        name=updated_faculty.name,
        age=updated_faculty.age,
        email=updated_faculty.email,
        department=updated_faculty.department
    )

    if result:
        print("Faculty updated successfully")
    else:
        print("Faculty not found")


@log_decorator
@time_decorator
def list_faculty():
    return db_get_all_faculty()
