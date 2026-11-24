
from app.utils.decorators import log_decorator, time_decorator


faculty_members = []


@log_decorator
@time_decorator
def add_faculty(faculty):
    faculty_members.append(faculty)
    print("Faculty added successfully")


@log_decorator
@time_decorator
def remove_faculty(faculty_id):
    for faculty in faculty_members:
        if faculty.faculty_id == faculty_id:
            faculty_members.remove(faculty)
            print("Faculty removed successfully")
            return

    print("Faculty not found")


@log_decorator
@time_decorator
def update_faculty(faculty_id, updated_faculty):
    for index, faculty in enumerate(faculty_members):
        if faculty.faculty_id == faculty_id:
            faculty_members[index] = updated_faculty
            print("Faculty updated successfully")
            return

    print("Faculty not found")


@log_decorator
@time_decorator
def list_faculty():
    return faculty_members
