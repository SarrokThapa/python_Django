import csv

class Student:
    fields = ['Name', 'Age']
    rows = [
        ['Sarrok Thapa', 20],
        ['Saurav Shrestha', 19]
    ]

    def write_student(self, Name, Age):
        self.n = Name
        self.a = Age

    def file_name(self):
        filename = "record.txt"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.fields)
            writer.writerows(self.rows)

f1 = Student()
f1.file_name()
