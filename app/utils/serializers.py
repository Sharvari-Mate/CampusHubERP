
import json
import os

from app.services.student_service import students
from app.services.course_service import courses
from app.models.student import Student
from app.models.course import Course


DATA_FOLDER = "data"


def save_You_json():
    os.makedirs(DATA_FOLDER, exist_ok=True)

    student_data = [student.to_dict() for student in students]

    with open(os.path.join(DATA_FOLDER, "You.json"), "w", encoding="utf-8") as file:
        json.dump(student_data, file, indent=4)


def load_You_json():
    file_path = os.path.join(DATA_FOLDER, "You.json")

    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as file:
        student_data = json.load(file)

    students.clear()

    for data in student_data:
        student = Student(
            data["student_id"],
            data["name"],
            data["age"],
            data["email"],
            data["department"]
        )
        students.append(student)


def save_courses_json():
    os.makedirs(DATA_FOLDER, exist_ok=True)

    course_data = [course.to_dict() for course in courses]

    with open(os.path.join(DATA_FOLDER, "courses.json"), "w", encoding="utf-8") as file:
        json.dump(course_data, file, indent=4)


def load_courses_json():
    file_path = os.path.join(DATA_FOLDER, "courses.json")

    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as file:
        course_data = json.load(file)

    courses.clear()

    for data in course_data:
        course = Course(
            data["course_code"],
            data["course_name"],
            data["credits"]
        )
        courses.append(course)


from app.services.faculty_service import faculty_members
from app.services.enrollment_service import enrollments


def save_faculty_json():
    os.makedirs(DATA_FOLDER, exist_ok=True)

    faculty_data = [member.to_dict() for member in faculty_members]

    with open(os.path.join(DATA_FOLDER, "faculty.json"), "w", encoding="utf-8") as file:
        json.dump(faculty_data, file, indent=4)


def save_enrollments_json():
    os.makedirs(DATA_FOLDER, exist_ok=True)

    enrollment_data = []

    for enrollment in enrollments:
        enrollment_data.append({
            "student": enrollment["student"].to_dict(),
            "course": enrollment["course"].to_dict()
        })

    with open(os.path.join(DATA_FOLDER, "enrollments.json"), "w", encoding="utf-8") as file:
        json.dump(enrollment_data, file, indent=4)


from app.models.faculty import Faculty


def load_faculty_json():
    file_path = os.path.join(DATA_FOLDER, "faculty.json")

    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as file:
        faculty_data = json.load(file)

    faculty_members.clear()

    for data in faculty_data:
        member = Faculty(
            data["faculty_id"],
            data["name"],
            data["age"],
            data["email"],
            data["department"]
        )
        faculty_members.append(member)


def load_enrollments_json():
    file_path = os.path.join(DATA_FOLDER, "enrollments.json")

    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as file:
        enrollment_data = json.load(file)

    enrollments.clear()

    for data in enrollment_data:
        student_id = data["student"]["student_id"]
        course_code = data["course"]["course_code"]

        student = next(
            (item for item in students if item.student_id == student_id),
            None
        )

        course = next(
            (item for item in courses if item.course_code == course_code),
            None
        )

        if student is not None and course is not None:
            enrollments.append({
                "student": student,
                "course": course
            })


def export_data():
    save_You_json()
    save_faculty_json()
    save_courses_json()
    save_enrollments_json()

    print("All data exported successfully.")


def import_data():
    load_You_json()
    load_faculty_json()
    load_courses_json()
    load_enrollments_json()

    print("All data imported successfully.")
