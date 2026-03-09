#A Dictionary is a mutable data structure that stoes dta in key-value pairs
#Dictionaries in pyton stores value as key value pairs
#The keys in dictionaries must be unique if the key repeats the data overites value of the old key
#The values can be duplicated
#The keys must be immutable
#the keys can be a string,int,float,tupule but it cannot be a list,dict,set
#we can use the dictionarie get method to get a default value if the key does not exist
#.get method is a safer one


#creating dictionaries
#ex d={"a":1,"b":2}
# dict() d-dict(a=1,b=2,c=3)
#d.keys() gives all thw keys in the variable d
#d.values()
#d.items() returns the key value pairs
#d.update to merge two dictionaries

#lets create a dictionary for student
student={"name":"Nikhil","age":23,"courses":["math","English"]}
print(student)
print(student["name"])
print(student["age"])

print(student.get("name")) #returns the value of the key
print(student.get("phone","Not found"))

#adding the key value to student dictionary
student["phone"]="12345-12345" #it adds the key value to the end of the dict

print(student) 

#to merge two dictionaries or add multiple values we use update
student.update({"City":"Bnagalore","state":"Karnataka"})
print(student)

#to delete a key value we use

del student["state"]
#or
student.pop("courses")

print(student)

#to find the length of dictionary
print(len(student))

print(student.keys()) #prints the keys in student dictionary

print(student.values()) #prints values in the student dictionary

print(student.items()) #prints the key value pairs in the student dictionarry
