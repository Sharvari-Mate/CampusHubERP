from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "sqlite:///campushub.db"


class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)

            cls._instance.engine = create_engine(
                DATABASE_URL,
                echo=False
            )

            cls._instance.SessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=cls._instance.engine
            )

        return cls._instance


database = DatabaseSingleton()

engine = database.engine
SessionLocal = database.SessionLocal

Base = declarative_base()
