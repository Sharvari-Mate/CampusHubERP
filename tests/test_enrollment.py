import unittest

from app.models.student import Student
from app.models.course import Course

from app.services.enrollment_service import (
    enroll_student,
    remove_enrollment,
    list_enrollments,
    enrollments
)

from database.repository import (
    add_student,
    delete_student,
    add_course,
    delete_course,
    delete_enrollment_by_student_course
)


class TestEnrollmentService(unittest.TestCase):

    def setUp(self):
        self.student = Student(
            "TEST_STU_901",
            "Test Student",
            19,
            "teststudent901@example.com",
            "Testing"
        )

        self.course = Course(
            "TEST901",
            "Test Course",
            3
        )

        # Clean up previous test records
        delete_enrollment_by_student_course(
            "TEST_STU_901",
            "TEST901"
        )

        delete_student("TEST_STU_901")
        delete_course("TEST901")

        # Add test Student and Course to the database
        add_student(self.student)
        add_course(self.course)

        enrollments.clear()

    def tearDown(self):
        delete_enrollment_by_student_course(
            "TEST_STU_901",
            "TEST901"
        )

        delete_student("TEST_STU_901")
        delete_course("TEST901")

        enrollments.clear()

    def test_enroll_student(self):
        enroll_student(self.student, self.course)

        records = list_enrollments()

        self.assertEqual(len(records), 1)
        self.assertEqual(
            records[0]["student"].student_id,
            "TEST_STU_901"
        )
        self.assertEqual(
            records[0]["course"].course_code,
            "TEST901"
        )

    def test_remove_enrollment(self):
        enroll_student(self.student, self.course)

        remove_enrollment(
            "TEST_STU_901",
            "TEST901"
        )

        records = list_enrollments()

        self.assertEqual(len(records), 0)

    def test_list_enrollments(self):
        enroll_student(self.student, self.course)

        records = list_enrollments()

        self.assertEqual(len(records), 1)

    def test_remove_nonexistent_enrollment(self):
        remove_enrollment(
            "NO_STUDENT",
            "NO_COURSE"
        )

        records = list_enrollments()

        self.assertEqual(len(records), 0)


if __name__ == "__main__":
    unittest.main()
