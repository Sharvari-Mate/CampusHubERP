from datetime import datetime
from abc import ABCMeta


class ModelMeta(ABCMeta):

    def __new__(mcs, name, bases, namespace):

        namespace["created_at"] = datetime.now
        namespace["updated_at"] = datetime.now

        return super().__new__(mcs, name, bases, namespace)
