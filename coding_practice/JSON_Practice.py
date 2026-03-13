#writing a program to ask for students name,age,course
#loading existing data from the json
#adding new student
#saving the json file back
import json

def add_student(Student):
        USN=input("Enter students USN: ")
        if USN in Student:
            print("The student with this usn already exists")
            y=int(input("""Do you want to update the student
                  1.Yes
                  2.No"""))
            if y==1:
                print("""Enter the value to be updated
                  1.s_name
                  2.s_age
                  3.exit""")
                up_valu=int(input("Enter the value from 1-3"))
                if up_valu==1:
                 up_nam=input("Enter the name to be updated")
                 Student[USN]["s_name"]=up_nam
                 print(Student)
                elif up_valu==2:
                 up_ag=int(input("Enter the updated age"))
                 Student[USN]["s_age"]=up_ag
                 print(Student)
                 return
            else:
                return

        name=input("Enter students name")
        age=int(input("Enter students age"))

        Student[USN]={"s_name":name,"s_age":age}
        print(f"Studentt {USN} is updated")
        print(Student)

def Update_student(Student):
             stu_upd=input("Enter the student usn to be updated")
             if stu_upd in Student:
              print("""Enter the value to be updated
                  1.s_name
                  2.s_age
                  3.exit""")
              up_value=int(input("Enter the value from 1-3"))
              if up_value==1:
                up_name=input("Enter the name to be updated")
                Student[stu_upd]["s_name"]=up_name
                print(Student)
              elif up_value==2:
                up_age=int(input("Enter the updated age"))
                Student[stu_upd]["s_age"]=up_age
                print(Student)

def delete_student(Student):
            stu_del=input("Enter the usn of the record to be deleted")
            if stu_del in Student:
             del Student[stu_del]
            else:
             print("the record is not present")

def load_data():
     try:
      with open("student_data.json","r") as f:
           return json.load(f)
     except:
          return{}
     
def save_data(Student):
     with open("student_data.json","w") as f:
          json.dump(Student,f,indent=4)
          


print("A STUDENTS DATABASE")

Student=load_data()
while True:
    print("""Enter the operation you wnat to perform
          1.Add a student
          2.update student record
          3.delete a student record
          4.exit""")
    try:
     input_1=int(input("Enter you choice from 1-4"))
    except ValueError:
        print("Please enter a valid number")
        continue
    if(input_1==1):
         add_student(Student)
         save_data(Student)
       
    
    elif input_1==2:
        Update_student(Student)
        save_data(Student)


    elif input_1==3:
         delete_student(Student)
         save_data(Student)
 
    elif input_1==4:
        print("student record turning offff")
        break
print(Student)

    # if(input==2):
    #     Up_usn=input("Enter the usn to be updated")
    #     if Up_usn in Student[USN]:
            

