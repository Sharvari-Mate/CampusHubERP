
import unittest
from secrets import randbelow

from app.models.faculty import Faculty
from app.services.faculty_service import (
    add_faculty,
    remove_faculty,
    update_faculty,
    list_faculty
)


class TestFacultyService(unittest.TestCase):

    def setUp(self):
        existing_ids = {
            faculty.faculty_id
            for faculty in list_faculty()
        }

        while True:
            faculty_id = f"FC{randbelow(900) + 100:03d}"
            if faculty_id not in existing_ids:
                break

        self.faculty_id = faculty_id

        self.faculty = Faculty(
            faculty_id=self.faculty_id,
            name="Test Faculty",
            age=35,
            email="testfaculty@example.com",
            department="Testing"
        )

    def tearDown(self):
        for faculty in list_faculty():
            if faculty.faculty_id == self.faculty_id:
                remove_faculty(self.faculty_id)
                break

    def test_add_faculty(self):
        add_faculty(self.faculty)

        faculty_records = list_faculty()

        self.assertTrue(
            any(
                faculty.faculty_id == self.faculty_id
                for faculty in faculty_records
            )
        )

    def test_update_faculty(self):
        add_faculty(self.faculty)

        updated_faculty = Faculty(
            faculty_id=self.faculty_id,
            name="Updated Test Faculty",
            age=36,
            email="updatedfaculty@example.com",
            department="Information Technology"
        )

        update_faculty(self.faculty_id, updated_faculty)

        faculty_records = list_faculty()

        found_faculty = next(
            faculty for faculty in faculty_records
            if faculty.faculty_id == self.faculty_id
        )

        self.assertEqual(found_faculty.name, "Updated Test Faculty")
        self.assertEqual(found_faculty.age, 36)
        self.assertEqual(
            found_faculty.department,
            "Information Technology"
        )

    def test_delete_faculty(self):
        add_faculty(self.faculty)

        remove_faculty(self.faculty_id)

        faculty_records = list_faculty()

        self.assertFalse(
            any(
                faculty.faculty_id == self.faculty_id
                for faculty in faculty_records
            )
        )

    def test_list_faculty(self):
        add_faculty(self.faculty)

        faculty_records = list_faculty()

        found_faculty = next(
            (
                faculty for faculty in faculty_records
                if faculty.faculty_id == self.faculty_id
            ),
            None
        )

        self.assertIsNotNone(found_faculty)


if __name__ == "__main__":
    unittest.main()
