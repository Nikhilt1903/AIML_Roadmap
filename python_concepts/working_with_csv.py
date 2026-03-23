# A CSV is defineed as comma seperated values
#it stores dtaa as a plain text file everthinng is considered as string
#each row in a file is a record and each column is a feild

#row 1=Header
#row 2+=data
#columns=seperated by commas

#csv is mostly used in
#datasets
#excel files
#data science projects
#API S

#its lightweight and easy to read/write

#we need to import csv module to use it 
import os
print(os.getcwd())

import csv

with open("AAPL.csv","r") as file:
    reader=csv.reader(file)
    
    for i in reader:
       print(i)

with open("AAPL.csv","r", newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)

import csv

with open("AAPL.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row)
with open("AAPL.csv","r") as file:
    reader = csv.reader(file)
    
    print(next(reader))  # 👈 should be header
    for i in reader:
        print(i)

#we can also print like
with open("AAPL.csv","r") as file:
    reader=csv.reader(file)

    for i in reader:
        print("Date:", i[0],"Open:",i[1])

#dictreader converts rows into dictionary and can be used to print the required rows
with open("AAPL.csv","r") as file:
    reader = csv.DictReader(file)
    
    for i in reader:
        print(i["Date"],i["Open"])

#small practice task
total=0
count=0
with open("AAPL.csv","r") as file:
    reader=csv.DictReader(file)

    for i in reader:
        to_do=float(i["Open"])

        if to_do>200:
            print(i["Date"],i["Open"])

        total=total+to_do
        count=count+1
average=total/count
print("The average of open is ",average)

# =================================================

#writing into csv files
#we use .writer to write into a file
#we use .writerow to write into ech row

import csv

with open("student.csv","w",newline="") as file:
    writer=csv.writer(file)

    writer.writerow(["name","age","marks"])
    writer.writerow(["alice",22,55])
    writer.writerow(["bob",23,90])

with open("student.csv","r") as file1:
    r=csv.reader(file1)

    for i in r:
        print(i)

with open("student.csv","a") as file2:
    a=csv.writer(file2)

    a.writerow(["charlie",21,28])

with open("student.csv","r") as file3:
    d=csv.reader(file3)

    for i in d:
        print(i)

# we can use writerows for writing into multiple records
#     writer.writerows([
#     ["alice",22,55],
#     ["bob",23,90]
# ])

import csv

# WRITE
with open("student.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows([
        {"name": "alice", "age": 22, "marks": 55},
        {"name": "bob", "age": 23, "marks": 90}
    ])

# READ
with open("student.csv", "r") as file:
    reader = csv.DictReader(file)
    max=0

    for row in reader:
        to_do=int(row["marks"])

        if to_do>50:
         print(row["name"], to_do)

        if to_do>max:
           max=to_do
print(f"the max marks is {row['name']} {max}")

