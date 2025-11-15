import csv

fields=['Name', 'Age', 'City']
rows=[
    ['Sarrok Thapa',20,'Kathmandu'],
    ['John Doe',25,'New York'],
    ['Jane Smith',30,'Los Angeles'],

]

filename = "a.txt"
with open (filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    