import re

from sqlalchemy.exc import IntegrityError

from database.db import SessionLocal
from database.models import (
    StudentDB,
    FacultyDB,
    CourseDB,
    EnrollmentDB
)


# VALIDATION FUNCTIONS

def is_valid_email(email):
    if not isinstance(email, str):
        return False

    return bool(
        re.fullmatch(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            email
        )
    )


def is_valid_course_code(course_code):
    if not isinstance(course_code, str):
        return False

    return bool(
        re.fullmatch(
            r"[A-Za-z0-9_-]{2,20}",
            course_code
        )
    )


# STUDENT FUNCTIONS

def add_student(student):
    session = SessionLocal()

    try:
        existing_student = session.get(
            StudentDB,
            student.student_id
        )

        if existing_student:
            print("Error: Student ID already exists")
            return None

        if not is_valid_email(student.email):
            print("Error: Invalid Email")
            return None

        record = StudentDB(
            student_id=student.student_id,
            name=student.name,
            age=student.age,
            email=student.email,
            department=student.department
        )

        session.add(record)
        session.commit()

        return record

    except IntegrityError:
        session.rollback()
        print("Error: Duplicate Student ID")
        return None

    except Exception as error:
        session.rollback()
        print(f"Error adding student: {error}")
        return None

    finally:
        session.close()


def get_You(student_id):
    session = SessionLocal()

    try:
        return session.get(StudentDB, student_id)

    finally:
        session.close()


def get_student(student_id):
    return get_You(student_id)


def update_student(student_id, **data):
    session = SessionLocal()

    try:
        record = session.get(StudentDB, student_id)

        if record is None:
            print("Error: Student not found")
            return None

        if "email" in data:
            if not is_valid_email(data["email"]):
                print("Error: Invalid Email")
                return None

        for key, value in data.items():
            if hasattr(record, key) and key != "student_id":
                setattr(record, key, value)

        session.commit()

        return record

    except Exception as error:
        session.rollback()
        print(f"Error updating student: {error}")
        return None

    finally:
        session.close()


def delete_student(student_id):
    session = SessionLocal()

    try:
        record = session.get(StudentDB, student_id)

        if record is None:
            print("Error: Student not found")
            return False

        session.delete(record)
        session.commit()

        return True

    except Exception as error:
        session.rollback()
        print(f"Error deleting student: {error}")
        return False

    finally:
        session.close()


# FACULTY FUNCTIONS

def add_faculty(faculty):
    session = SessionLocal()

    try:
        if not is_valid_email(faculty.email):
            print("Error: Invalid Email")
            return None

        record = FacultyDB(
            faculty_id=faculty.faculty_id,
            name=faculty.name,
            age=faculty.age,
            email=faculty.email,
            department=faculty.department
        )

        session.add(record)
        session.commit()

        return record

    except IntegrityError:
        session.rollback()
        print("Error: Faculty ID already exists")
        return None

    except Exception as error:
        session.rollback()
        print(f"Error adding faculty: {error}")
        return None

    finally:
        session.close()


def get_faculty(faculty_id):
    session = SessionLocal()

    try:
        return session.get(FacultyDB, faculty_id)

    finally:
        session.close()


def update_faculty(faculty_id, **data):
    session = SessionLocal()

    try:
        record = session.get(FacultyDB, faculty_id)

        if record is None:
            print("Error: Faculty not found")
            return None

        if "email" in data:
            if not is_valid_email(data["email"]):
                print("Error: Invalid Email")
                return None

        for key, value in data.items():
            if hasattr(record, key) and key != "faculty_id":
                setattr(record, key, value)

        session.commit()

        return record

    except Exception as error:
        session.rollback()
        print(f"Error updating faculty: {error}")
        return None

    finally:
        session.close()


def delete_faculty(faculty_id):
    session = SessionLocal()

    try:
        record = session.get(FacultyDB, faculty_id)

        if record is None:
            print("Error: Faculty not found")
            return False

        session.delete(record)
        session.commit()

        return True

    except Exception as error:
        session.rollback()
        print(f"Error deleting faculty: {error}")
        return False

    finally:
        session.close()


# COURSE FUNCTIONS

def add_course(course):
    session = SessionLocal()

    try:
        if not is_valid_course_code(course.course_code):
            print("Error: Invalid Course Code")
            return None

        existing_course = session.get(
            CourseDB,
            course.course_code
        )

        if existing_course:
            print("Error: Course Code already exists")
            return None

        record = CourseDB(
            course_code=course.course_code,
            course_name=course.course_name,
            credits=course.credits
        )

        session.add(record)
        session.commit()

        return record

    except IntegrityError:
        session.rollback()
        print("Error: Course Code already exists")
        return None

    except Exception as error:
        session.rollback()
        print(f"Error adding course: {error}")
        return None

    finally:
        session.close()


def get_course(course_code):
    session = SessionLocal()

    try:
        return session.get(CourseDB, course_code)

    finally:
        session.close()


def update_course(course_code, **data):
    session = SessionLocal()

    try:
        record = session.get(CourseDB, course_code)

        if record is None:
            print("Error: Course not found")
            return None

        for key, value in data.items():
            if hasattr(record, key) and key != "course_code":
                setattr(record, key, value)

        session.commit()

        return record

    except Exception as error:
        session.rollback()
        print(f"Error updating course: {error}")
        return None

    finally:
        session.close()


def delete_course(course_code):
    session = SessionLocal()

    try:
        record = session.get(CourseDB, course_code)

        if record is None:
            print("Error: Course not found")
            return False

        session.delete(record)
        session.commit()

        return True

    except Exception as error:
        session.rollback()
        print(f"Error deleting course: {error}")
        return False

    finally:
        session.close()


# ENROLLMENT FUNCTIONS

def add_enrollment(student_id, course_code):
    session = SessionLocal()

    try:
        student = session.get(StudentDB, student_id)

        if student is None:
            print("Error: Student not found")
            return None

        if not is_valid_course_code(course_code):
            print("Error: Invalid Course Code")
            return None

        course = session.get(CourseDB, course_code)

        if course is None:
            print("Error: Course not found")
            return None

        record = EnrollmentDB(
            student_id=student_id,
            course_code=course_code
        )

        session.add(record)
        session.commit()

        print("Enrollment created successfully")

        return record

    except IntegrityError:
        session.rollback()
        print("Error: Enrollment already exists or is invalid")
        return None

    except Exception as error:
        session.rollback()
        print(f"Error creating enrollment: {error}")
        return None

    finally:
        session.close()


def get_enrollments():
    session = SessionLocal()

    try:
        return session.query(EnrollmentDB).all()

    finally:
        session.close()


def delete_enrollment(enrollment_id):
    session = SessionLocal()

    try:
        record = session.get(EnrollmentDB, enrollment_id)

        if record is None:
            print("Error: Enrollment not found")
            return False

        session.delete(record)
        session.commit()

        return True

    except Exception as error:
        session.rollback()
        print(f"Error deleting enrollment: {error}")
        return False

    finally:
        session.close()


def delete_enrollment_by_student_course(student_id, course_code):
    session = SessionLocal()

    try:
        record = session.query(EnrollmentDB).filter_by(
            student_id=student_id,
            course_code=course_code
        ).first()

        if record is None:
            print("Error: Enrollment not found")
            return False

        session.delete(record)
        session.commit()

        return True

    except Exception as error:
        session.rollback()
        print(f"Error deleting enrollment: {error}")
        return False

    finally:
        session.close()


# GET ALL FUNCTIONS

def get_all_students():
    session = SessionLocal()

    try:
        return session.query(StudentDB).all()

    finally:
        session.close()


def get_all_faculty():
    session = SessionLocal()

    try:
        return session.query(FacultyDB).all()

    finally:
        session.close()


def get_all_courses():
    session = SessionLocal()

    try:
        return session.query(CourseDB).all()

    finally:
        session.close()


def get_all_enrollments():
    return get_enrollments()
