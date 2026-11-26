
import re


def validate_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_student_id(student_id):
    pattern = r"^ST\d{3}$"
    return re.match(pattern, student_id) is not None


def validate_faculty_id(faculty_id):
    pattern = r"^FC\d{3}$"
    return re.match(pattern, faculty_id) is not None


def validate_course_code(course_code):
    pattern = r"^CS\d{3}$"
    return re.match(pattern, course_code) is not None
