
from flask import Blueprint, request, jsonify

from app.models.course import Course

from app.services.course_service import (
    add_course,
    remove_course,
    update_course,
    list_courses
)


course_api = Blueprint("course_api", __name__)


def course_to_dict(course):
    return {
        "course_code": course.course_code,
        "course_name": course.course_name,
        "credits": course.credits
    }


@course_api.route("/courses", methods=["GET"])
def get_courses():
    courses = list_courses()
    return jsonify([course_to_dict(course) for course in courses])


@course_api.route("/courses/<course_code>", methods=["GET"])
def get_course(course_code):
    for course in list_courses():
        if course.course_code == course_code:
            return jsonify(course_to_dict(course))

    return jsonify({"error": "Course not found"}), 404


@course_api.route("/courses", methods=["POST"])
def create_course():
    data = request.get_json()

    course = Course(
        course_code=data["course_code"],
        course_name=data["course_name"],
        credits=int(data["credits"])
    )

    add_course(course)

    return jsonify({
        "message": "Course added successfully",
        "course": course_to_dict(course)
    }), 201


@course_api.route("/courses/<course_code>", methods=["PUT"])
def edit_course(course_code):
    data = request.get_json()

    updated_course = Course(
        course_code=course_code,
        course_name=data["course_name"],
        credits=int(data["credits"])
    )

    update_course(course_code, updated_course)

    return jsonify({
        "message": "Course updated successfully",
        "course": course_to_dict(updated_course)
    })


@course_api.route("/courses/<course_code>", methods=["DELETE"])
def delete_course(course_code):
    remove_course(course_code)

    return jsonify({
        "message": "Course delete request completed",
        "course_code": course_code
    })
