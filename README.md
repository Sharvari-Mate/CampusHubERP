
# CampusHub ERP

CampusHub ERP is a backend application for managing students, faculty, courses, and enrollments.

## Features
- Student Management
- Faculty Management
- Course Management
- Enrollment Management
- SQLite Database
- SQLAlchemy ORM
- REST APIs
- Data Validation
- JSON Import and Export
- Report Generation
- Logging
- Unit Testing

## Technologies Used
- Python
- Flask
- SQLite
- SQLAlchemy

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m app.main
```

## Database
The application uses SQLite database `campushub.db`.

## Logs
Application logs are stored in `logs/application.log`.

## Tests
Run unit tests using:

```bash
python -m unittest discover -s tests -v
```
