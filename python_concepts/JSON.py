# JSON = java script object notationn 

# its a text based format used to store structured Data 

# a json file looks like 
{
    "name":'Nikhil',
    "Age":24,
    "Skills":["Python","Sql"]
}

# Json is basically used for :
#  Storing data
#  transferring data between files
#  API 
#  Configuration files 

#python datats vs JSON

# py              JSON
#  dict            object
#  list            array
#  str             string    
#  int/float       number     
#  True            true
#  False           false
#  None            null

#we must import json module to work on it
import json

#json.dump() write the python object to json file
#json.load() read json file into python object
#json.dumps() covert object to json string
#json.loads() convert json string to object

#writing json files
import json

students={"nikhil":90,"Karthik":95}

with open("File.json","w") as f:
    json.dump(students,f,indent=4) #indent is used make the program much readable it add 4 indent spaces after eact object in the dictionsy

#reading a file from json
with open("File.json","r") as m:
    data=json.load(m)

print(data)

print(data["nikhil"])
#we cannot use appen in json becaue json should have one root object
#insted we must load the file and update the data and write to the file again

#ahandling missinf files in json

#the code below opens a file if file exisits in the system apath it opens the file else without thrwing an error it create a new dictionaru
try:
    with open("new_jsonjson","r") as r:
        data=json.load(f)
except FileNotFoundError:
    data={}

#limitations of json
#it cannot store sets,tuples,functions,custom objects

# JSON is used in:

# REST APIs
# web applications
# machine learning configuration
# databases
# mobile apps
# cloud systems