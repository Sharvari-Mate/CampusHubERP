
from app.utils.decorators import log_decorator, time_decorator

from app.utils.logger import (
    log_course_added,
    log_error
)

from database.repository import (
    add_course as db_add_course,
    get_course as db_get_course,
    update_course as db_update_course,
    delete_course as db_delete_course,
    get_all_courses as db_get_all_courses
)


@log_decorator
@time_decorator
def add_course(course):
    try:
        result = db_add_course(course)

        if result:
            log_course_added(course.course_code)
            print("Course added successfully")

    except Exception as error:
        log_error(f"Error adding course: {error}")
        raise


@log_decorator
@time_decorator
def remove_course(course_code):
    result = db_delete_course(course_code)

    if result:
        print("Course removed successfully")
    else:
        print("Course not found")


@log_decorator
@time_decorator
def update_course(course_code, updated_course):
    result = db_update_course(
        course_code,
        course_name=updated_course.course_name,
        credits=updated_course.credits
    )

    if result:
        print("Course updated successfully")
    else:
        print("Course not found")


@log_decorator
@time_decorator
def list_courses():
    return db_get_all_courses()
