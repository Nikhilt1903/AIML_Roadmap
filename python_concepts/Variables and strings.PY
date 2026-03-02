message="Hellow world" #message is the variable
print(message)

#we use triple quotes for multi line statement
vari="""hi my name is nikhil
i am 2024 grad"""
print(vari)

#index example
print(message[0]) #prints the value at that index

print(message[0:5])#prints the value from index 0-4 but excludes 5th

print(message[:5])#prints the enire word from starting to 4th index

print(message[7:])#prints from index 7 to entire word

print(message.lower()) #prints the lower case of mesage
print(message.upper()) #prints the upper case of message
print(message)
print(message.count("Hellow")) #returns the count of word hellow in our variable
print(message.count("l")) #returns the count of l in our variable 

print(message.find("l")) #returns the index of the occurance of first l in our variable
print(message.find('universe')) #returns -1 if the word or letter is not there in the variable

message1=message.replace("Hello","Universe") #using replace
print(message1)

message= "hello"+" "+"Nikhil"+" "+"Welcome!"#using concat with "+"
print(message)

#using fstring placeholders insted of using plus to stop being messy
greeting="Hello"
name="Nikhil"
message= f'{greeting} {name} welcome'
print(message)

print(dir(name)) #gives all the methods that can be performed on name
print(help(str)) #gives all the methods with what it does on given datatype
print(help(str.lower)) #gives the help for only lower method
