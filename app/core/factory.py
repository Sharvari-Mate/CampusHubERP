from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course


class EntityFactory:
    @staticmethod
    def create_entity(entity_type, **data):
        entity_type = entity_type.lower()

        if entity_type == "student":
            return Student(**data)

        elif entity_type == "faculty":
            return Faculty(**data)

        elif entity_type == "course":
            return Course(**data)

        else:
            raise ValueError("Invalid entity type")
