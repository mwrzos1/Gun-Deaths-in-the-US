

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

#extract years from column 2 

years = [row[1] for row in data]
year_counts= {}

# each time element is a key in dictionary add 1
for element in years:
    if element in year_counts:
        year_counts[element] = year_counts[element] + 1
    else:
        year_counts[element] = 1
print(year_counts)