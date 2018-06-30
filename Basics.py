

#import file and display first 5 rows

import csv
file=open("guns.csv", "r")
csvreader= csv.reader(file)
data= list(csvreader)
print(data[0:5])

#remove header and print first 5 rows

headers = data[0:1]
data = data[1:]
print(headers)
print(data[0:5])  