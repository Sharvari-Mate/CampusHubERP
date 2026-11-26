
from flask import Blueprint, request, jsonify

from app.services.enrollment_service import (
    enroll_student,
    remove_enrollment,
    list_enrollments
)

from app.services.student_service import list_students
from app.services.course_service import list_courses


enrollment_api = Blueprint("enrollment_api", __name__)


def enrollment_to_dict(enrollment):
    student = enrollment["student"]
    course = enrollment["course"]

    return {
        "enrollment_id": f"{student.student_id}-{course.course_code}",
        "student_id": student.student_id,
        "student_name": student.name,
        "course_code": course.course_code,
        "course_name": course.course_name
    }


@enrollment_api.route("/enrollments", methods=["GET"])
def get_enrollments():
    records = list_enrollments()

    return jsonify([
        enrollment_to_dict(enrollment)
        for enrollment in records
    ])


@enrollment_api.route("/enrollments", methods=["POST"])
def create_enrollment():
    data = request.get_json()

    student_id = data["student_id"]
    course_code = data["course_code"]

    student = None
    course = None

    for item in list_students():
        if item.student_id == student_id:
            student = item
            break

    for item in list_courses():
        if item.course_code == course_code:
            course = item
            break

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    if course is None:
        return jsonify({"error": "Course not found"}), 404

    enroll_student(student, course)

    return jsonify({
        "message": "Enrollment created successfully",
        "enrollment": {
            "enrollment_id": f"{student_id}-{course_code}",
            "student_id": student_id,
            "course_code": course_code
        }
    }), 201


@enrollment_api.route(
    "/enrollments/<enrollment_id>",
    methods=["DELETE"]
)
def delete_enrollment(enrollment_id):
    try:
        student_id, course_code = enrollment_id.split("-", 1)
    except ValueError:
        return jsonify({
            "error": "Invalid enrollment ID. Use STUDENTID-COURSECODE."
        }), 400

    remove_enrollment(student_id, course_code)

    return jsonify({
        "message": "Enrollment delete request completed",
        "enrollment_id": enrollment_id
    })
