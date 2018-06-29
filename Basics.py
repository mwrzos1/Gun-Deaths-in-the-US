

#import file and display the first 5 rows


import csv
file=open("guns.csv", "r")
csvreader= csv.reader(file)
data= list(csvreader)
print(data[0:5])


