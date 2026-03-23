#using csv to read and write using dict reader
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