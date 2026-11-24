
from app.services.student_service import students
from app.services.faculty_service import faculty_members
from app.services.course_service import courses


def student_report():
    for student in students:
        yield student


def faculty_report():
    for faculty in faculty_members:
        yield faculty


def course_report():
    for course in courses:
        yield course
