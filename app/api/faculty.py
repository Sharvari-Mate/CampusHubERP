
from flask import Blueprint, request, jsonify

from app.models.faculty import Faculty
from app.services.faculty_service import (
    add_faculty,
    remove_faculty,
    update_faculty,
    list_faculty
)


faculty_api = Blueprint("faculty_api", __name__)


def faculty_to_dict(faculty):
    return {
        "faculty_id": faculty.faculty_id,
        "name": faculty.name,
        "age": faculty.age,
        "email": faculty.email,
        "department": faculty.department
    }


@faculty_api.route("/faculty", methods=["GET"])
def get_faculty_list():
    faculty_members = list_faculty()

    return jsonify([
        faculty_to_dict(faculty)
        for faculty in faculty_members
    ])


@faculty_api.route("/faculty/<faculty_id>", methods=["GET"])
def get_faculty_by_id(faculty_id):
    for faculty in list_faculty():
        if faculty.faculty_id == faculty_id:
            return jsonify(faculty_to_dict(faculty))

    return jsonify({"error": "Faculty not found"}), 404


@faculty_api.route("/faculty", methods=["POST"])
def create_faculty():
    data = request.get_json()

    faculty = Faculty(
        faculty_id=data["faculty_id"],
        name=data["name"],
        age=int(data["age"]),
        email=data["email"],
        department=data["department"]
    )

    add_faculty(faculty)

    return jsonify({
        "message": "Faculty added successfully",
        "faculty": faculty_to_dict(faculty)
    }), 201


@faculty_api.route("/faculty/<faculty_id>", methods=["PUT"])
def edit_faculty(faculty_id):
    data = request.get_json()

    updated_faculty = Faculty(
        faculty_id=faculty_id,
        name=data["name"],
        age=int(data["age"]),
        email=data["email"],
        department=data["department"]
    )

    update_faculty(faculty_id, updated_faculty)

    return jsonify({
        "message": "Faculty updated successfully",
        "faculty": faculty_to_dict(updated_faculty)
    })


@faculty_api.route("/faculty/<faculty_id>", methods=["DELETE"])
def delete_faculty(faculty_id):
    remove_faculty(faculty_id)

    return jsonify({
        "message": "Faculty delete request completed",
        "faculty_id": faculty_id
    })
