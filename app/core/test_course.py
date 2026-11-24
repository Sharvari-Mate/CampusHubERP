from app.models.course import Course

course = Course("CS101", "Python Programming", 4)

print("COURSE DETAILS")
course.display_details()

print("\nCOURSE DICTIONARY")
print(course.to_dict())

print("\nCOURSE MODEL TEST COMPLETED")
