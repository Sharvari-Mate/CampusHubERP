
def make_id_generator(prefix):
    counter = 0

    def generate_id():
        nonlocal counter
        counter += 1
        return f"{prefix}{counter:03d}"

    return generate_id


generate_student_id = make_id_generator("ST")
generate_faculty_id = make_id_generator("FC")
generate_course_id = make_id_generator("CS")
