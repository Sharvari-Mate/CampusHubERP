
from database.db import engine, SessionLocal, Base
from database import models


Base.metadata.create_all(bind=engine)

with engine.connect() as connection:
    print("SQLite database connected successfully.")

session = SessionLocal()
print("Database session created successfully.")
session.close()

print("Database tables created successfully.")
print("Week 7 Step 2 test completed.")
