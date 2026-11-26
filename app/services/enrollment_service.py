from app.utils.decorators import log_decorator, time_decorator

from app.utils.logger import (
    log_enrollment_created,
    log_error
)

from database.repository import (
    add_enrollment as repository_add_enrollment,
    delete_enrollment_by_student_course,
    get_enrollments as repository_get_enrollments
)


enrollments = []


@log_decorator
@time_decorator
def enroll_student(student, course):
    try:
        result = repository_add_enrollment(
            student.student_id,
            course.course_code
        )

        if result:
            enrollment = {
                "student": student,
                "course": course
            }

            enrollments.append(enrollment)

            log_enrollment_created(
                student.student_id,
                course.course_code
            )

            print("Student enrolled successfully")

    except Exception as error:
        log_error(f"Error creating enrollment: {error}")
        raise


@log_decorator
@time_decorator
def remove_enrollment(student_id, course_code):
    try:
        result = delete_enrollment_by_student_course(
            student_id,
            course_code
        )

        if result:
            enrollments[:] = [
                enrollment
                for enrollment in enrollments
                if not (
                    enrollment["student"].student_id == student_id
                    and enrollment["course"].course_code == course_code
                )
            ]

            print("Enrollment removed successfully")
        else:
            print("Enrollment not found")

    except Exception as error:
        log_error(f"Error deleting enrollment: {error}")
        raise


@log_decorator
@time_decorator
def list_enrollments():
    return enrollments
