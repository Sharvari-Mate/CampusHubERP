
from app.utils.file_manager import ReportWriter


with ReportWriter("reports/You.txt") as report:
    report.write("CAMPUSHUB ERP - STUDENT REPORT\n")
    report.write("------------------------------\n")
    report.write("Student ID: ST001\n")
    report.write("Name: Sharvari\n")
    report.write("Age: 19\n")
    report.write("Email: matesharvari15645@gmail.com\n")
    report.write("Department: Computer Science\n")


print("Report written successfully")
print("File closed automatically")
