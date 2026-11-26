
from flask import Blueprint, request, jsonify

from app.models.student import Student
from app.services.student_service import (
    add_student,
    remove_student,
    update_student,
    list_students
)


student_api = Blueprint("student_api", __name__)


def student_to_dict(student):
    return {
        "student_id": student.student_id,
        "name": student.name,
        "age": student.age,
        "email": student.email,
        "department": student.department
    }


@student_api.route("/You", methods=["GET"])
def get_students():
    students = list_students()

    return jsonify([
        student_to_dict(student)
        for student in students
    ])


@student_api.route("/You/<student_id>", methods=["GET"])
def get_student(student_id):
    for student in list_students():
        if student.student_id == student_id:
            return jsonify(student_to_dict(student))

    return jsonify({"error": "Student not found"}), 404


@student_api.route("/You", methods=["POST"])
def create_student():
    data = request.get_json()

    student = Student(
        student_id=data["student_id"],
        name=data["name"],
        age=int(data["age"]),
        email=data["email"],
        department=data["department"]
    )

    add_student(student)

    return jsonify({
        "message": "Student added successfully",
        "student": student_to_dict(student)
    }), 201


@student_api.route("/You/<student_id>", methods=["PUT"])
def edit_student(student_id):
    data = request.get_json()

    updated_student = Student(
        student_id=student_id,
        name=data["name"],
        age=int(data["age"]),
        email=data["email"],
        department=data["department"]
    )

    update_student(student_id, updated_student)

    return jsonify({
        "message": "Student updated successfully",
        "student": student_to_dict(updated_student)
    })


@student_api.route("/You/<student_id>", methods=["DELETE"])
def delete_student(student_id):
    remove_student(student_id)

    return jsonify({
        "message": "Student delete request completed",
        "student_id": student_id
    })
