import csv

fields = ['Name','Marks']
rows = [['Sarrok',85],
        ['SAurav',90], 
        ['Charlie',55],
        ['David',92],
        ['Eva',60]]

with open('students_marks.csv', 'w', newline='') as file:
    csvwriter= csv.writer(file)
    csvwriter.writerow(fields)  
    csvwriter.writerows(rows)