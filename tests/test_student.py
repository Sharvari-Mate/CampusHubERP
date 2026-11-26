
import unittest
from secrets import randbelow

from app.models.student import Student
from app.services.student_service import (
    add_student,
    remove_student,
    update_student,
    list_students
)


class TestStudentService(unittest.TestCase):

    def setUp(self):
        existing_ids = {
            student.student_id
            for student in list_students()
        }

        while True:
            student_id = f"ST{randbelow(900) + 100:03d}"
            if student_id not in existing_ids:
                break

        self.student_id = student_id

        self.student = Student(
            student_id=self.student_id,
            name="Test Student",
            age=19,
            email="teststudent@example.com",
            department="Testing"
        )

    def tearDown(self):
        for student in list_students():
            if student.student_id == self.student_id:
                remove_student(self.student_id)
                break

    def test_add_student(self):
        add_student(self.student)

        student_records = list_students()

        self.assertTrue(
            any(
                student.student_id == self.student_id
                for student in student_records
            )
        )

    def test_update_student(self):
        add_student(self.student)

        updated_student = Student(
            student_id=self.student_id,
            name="Updated Test Student",
            age=20,
            email="updatedstudent@example.com",
            department="Information Technology"
        )

        update_student(self.student_id, updated_student)

        student_records = list_students()

        found_student = next(
            student for student in student_records
            if student.student_id == self.student_id
        )

        self.assertEqual(found_student.name, "Updated Test Student")
        self.assertEqual(found_student.age, 20)
        self.assertEqual(
            found_student.department,
            "Information Technology"
        )

    def test_delete_student(self):
        add_student(self.student)

        remove_student(self.student_id)

        student_records = list_students()

        self.assertFalse(
            any(
                student.student_id == self.student_id
                for student in student_records
            )
        )

    def test_list_students(self):
        add_student(self.student)

        student_records = list_students()

        found_student = next(
            (
                student for student in student_records
                if student.student_id == self.student_id
            ),
            None
        )

        self.assertIsNotNone(found_student)


if __name__ == "__main__":
    unittest.main()
