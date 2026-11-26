
import unittest
import uuid


from app.models.course import Course
from app.services.course_service import (
    add_course,
    remove_course,
    update_course,
    list_courses
)


class TestCourseService(unittest.TestCase):

    def setUp(self):
        self.course_code = "T" + uuid.uuid4().hex[:7].upper()
        self.course = Course(
            self.course_code,
            "Test Course",
            3
        )

    def tearDown(self):
        remove_course(self.course_code)

    def test_add_course(self):
        add_course(self.course)

        courses = list_courses()
        course_codes = [course.course_code for course in courses]

        self.assertIn(self.course_code, course_codes)

    def test_update_course(self):
        add_course(self.course)

        updated_course = Course(
            self.course_code,
            "Updated Test Course",
            4
        )

        update_course(self.course_code, updated_course)

        courses = list_courses()
        course = next(
            course for course in courses
            if course.course_code == self.course_code
        )

        self.assertEqual(course.course_name, "Updated Test Course")
        self.assertEqual(course.credits, 4)

    def test_delete_course(self):
        add_course(self.course)

        remove_course(self.course_code)

        courses = list_courses()
        course_codes = [course.course_code for course in courses]

        self.assertNotIn(self.course_code, course_codes)

    def test_list_courses(self):
        add_course(self.course)

        courses = list_courses()
        course_codes = [course.course_code for course in courses]

        self.assertIn(self.course_code, course_codes)


if __name__ == "__main__":
    unittest.main()
