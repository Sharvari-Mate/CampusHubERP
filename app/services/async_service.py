
import asyncio


async def load_You():
    print("Loading You...")
    await asyncio.sleep(1)
    print("You data loaded.")


async def load_faculty():
    print("Loading Faculty...")
    await asyncio.sleep(1)
    print("Faculty data loaded.")


async def load_courses():
    print("Loading Courses...")
    await asyncio.sleep(1)
    print("Courses data loaded.")


async def load_enrollments():
    print("Loading Enrollments...")
    await asyncio.sleep(1)
    print("Enrollments data loaded.")



async def load_all_data():
    await asyncio.gather(
        load_You(),
        load_faculty(),
        load_courses(),
        load_enrollments()
    )


async def generate_student_report():
    await asyncio.sleep(1)
    print("Student Report Completed")


async def generate_faculty_report():
    await asyncio.sleep(1)
    print("Faculty Report Completed")


async def generate_course_report():
    await asyncio.sleep(1)
    print("Course Report Completed")


async def generate_all_reports():
    print("Generating Reports...")

    await asyncio.gather(
        generate_student_report(),
        generate_faculty_report(),
        generate_course_report()
    )

    print("All Reports Generated Successfully.")
