courses = []


def add_course(course):
    courses.append(course)
    print("Course added successfully")


def remove_course(course_code):
    for course in courses:
        if course.course_code == course_code:
            courses.remove(course)
            print("Course removed successfully")
            return

    print("Course not found")


def update_course(course_code, updated_course):
    for index, course in enumerate(courses):
        if course.course_code == course_code:
            courses[index] = updated_course
            print("Course updated successfully")
            return

    print("Course not found")


def list_courses():
    return courses
