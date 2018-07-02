

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

#  list comprehension to get result for year and month
import datetime
dates = [datetime.datetime (year=int(row[1]), month=int(row[2]), day=1) for row in data]
print(dates[0:5])


# count how many times each unique date occurs in dates
date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] = date_counts[date]+1
    else:
        date_counts[date]=1
print(date_counts)

#count how many times each unique gender appears in sex
sex = [row[5] for row in data]
sex_counts ={}
for gender in sex:
    if gender in sex_counts:
        sex_counts[gender]= sex_counts[gender]+1
    else:
        sex_counts[gender] = 1
print(sex_counts)

#count how many times each unique ethnicity appears in race
race = [row[7] for row in data]
race_counts={}
for ethnicity in race:
    if ethnicity in race_counts:
        race_counts[ethnicity]= race_counts[ethnicity]+1
    else:
        race_counts[ethnicity]=1
print(race_counts)

#import file census.csv and convert to list of lists
import csv
file = open("census.csv", "r")
csv_reader = csv.reader(file)
census = list(csv_reader)
print(census)