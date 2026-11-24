
from app.services.student_service import students


class StudentIterator:

    def __init__(self, student_list):
        self.student_list = student_list
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.student_list):
            raise StopIteration

        student = self.student_list[self.index]
        self.index += 1

        return student
