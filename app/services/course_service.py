
from app.utils.decorators import log_decorator, time_decorator


courses = []


@log_decorator
@time_decorator
def add_course(course):
    courses.append(course)
    print("Course added successfully")


@log_decorator
@time_decorator
def remove_course(course_code):
    for course in courses:
        if course.course_code == course_code:
            courses.remove(course)
            print("Course removed successfully")
            return

    print("Course not found")


@log_decorator
@time_decorator
def update_course(course_code, updated_course):
    for index, course in enumerate(courses):
        if course.course_code == course_code:
            courses[index] = updated_course
            print("Course updated successfully")
            return

    print("Course not found")


@log_decorator
@time_decorator
def list_courses():
    return courses
