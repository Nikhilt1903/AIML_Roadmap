#basic dictionaries practice

#creating a dictiary with my details
my_det={"first_name":"Nikhil","Lat_name":"Talapaneni","age":23,"City":"Bangalore"}
print(my_det)
print(my_det["first_name"])
print(my_det["age"])
print(my_det.get("city","not found in ther dict"))


print("Welcome to the student dictionary")

students={}

USN=input("Enter the usn of the student")
name=input("Enter the name of the student")
age=int(input("enter the age of the student"))
sem=int(input("Enter the semester of the student"))

students[USN]={"name":name,"age":age,"sem":sem}
print(students)
# n=int(print(""" Enter thr number of student details to be entered
#       """))
# for n in range(n):
    
print("""Do you wnat perform more operations
      Y=yes
      N=no""")
agr=input("Enter Y or N")
if agr=="Y":
 while True:
 
    print("""Enter the operation you want to perform
          1.Add more students
          2.Udate the record of a student
          3.Remove a record of the student
          4.search for a student
          5.Exit""")
    choice=int(input("Enter you choice from 1-5"))
    if choice==1:
        count_s=int(input(("Enter the number of students record you want to enter")))
        for i in range(count_s):
            USN=input("Enter the usn of the student")
            name=input("Enter the name of the student")
            age=int(input("enter the age of the student"))
            sem=int(input("Enter the semester of the student")) 
            students[USN]={"name":name,"age":age,"sem":sem}
            print(students)
        print(f""" The recorde after updation is 
              {students}""")
        
    elif choice==2:
        stu_ex=input("Enter the usn to be updated")
        if stu_ex in students:
            num_up=int(input("""Enter the number of values you want to update from
                     name
                     age
                     sem"""))
            for i in range(num_up):
              
              print("""Enter the value you want to update
                     1.name
                     2.age
                     3.sem""")
              ch=int(input("Enter your choic from1_3"))
              if ch==1:
                  students[stu_ex]["name"]=input("Enter the value")
              elif ch==2:
                  students[stu_ex]["age"]=int(input("Enter the value"))
              elif ch==3:
                  students[stu_ex]["sem"]=int(input("Enter the value")) 
        else:
                  print("Usn not found in students") 
         
    elif choice==3:
        stu_del=input("Enter the Usn you want to delete")
        if stu_del in students:
            del students[stu_del]
        else:
            print("The Usn is not in the records")

    elif choice==4:
        stu_sear=input("Enter the usn you want to search")
        if stu_sear in students:
            print(students[stu_sear])
        else:
            print("The student recod does not exist")

    elif choice==5:
        print("Exiting the program")
        break

   
print(f"Updated student list is {students} ") 
for key in students.keys():
    print(f"The details of {key} is")
    print(f"Name = {students[key]['name']}")
    print(f"Age = {students[key]['age']}")
    print(f"Sem = {students[key]['sem']}")
    print()    

#counting the ferequency of words

sentence=input("Enter the sentence: ")
words=sentence.split()
print(words)

freque={}

for i in words:
    if i in freque:
        freque[i]+=1
    else:
        freque[i]=1

for key,value in freque.items():
    print(f"{key} is repeated {value} times")


#Students marks using dictonaries
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88
}
split_1=students.values()
print(f"the highest marks in the class is {max(split_1)}")
print(f"The average marks in the class is {sum(split_1)/len(split_1)}")
print(max(students, key=students.get))
for key,value in students.items():
    print(f"{key} marsk is {value}")


