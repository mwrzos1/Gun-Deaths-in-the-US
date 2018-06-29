
# coding: utf-8

# In[9]:


import csv
file=open("guns.csv", "r")
csvreader= csv.reader(file)
data= list(csvreader)
print(data[0:5])


