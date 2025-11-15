import csv
import os

class Student:
    def __init__(self):
        self.fields = ['Name', 'Age']

    def write_student(self, Name, Age):
        student_record = {
            'Name': Name,
            'Age': Age
        }

        filename = "record.csv"

        # open in a+ (append + read)
        with open(filename, "a+", newline='') as file:
            file.seek(0)  # move to start so we can read
            content = file.read().strip()

            writer = csv.DictWriter(file, fieldnames=self.fields)

            # write header only if file is empty
            if content == "":
                writer.writeheader()

            # write the record
            writer.writerow(student_record)


# ---- TEST ----
s = Student()
s.write_student("Sarrok Thapa", 20)
s.write_student("Saurav Shrestha", 19)
