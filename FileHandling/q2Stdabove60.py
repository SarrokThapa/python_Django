import csv


# Read the original file and filter students with marks > 60
high_scorers = [["Name", "Marks"]]  # Header for the new file

with open('students_marks.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        name = row[0]
        marks = int(row[1])  
        if marks > 60:
            high_scorers.append([name, marks])


with open('high_scorers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(high_scorers)

print("high_scorers.csv has been created ")