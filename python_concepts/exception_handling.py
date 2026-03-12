#Exception handling in python
#exception handling is a way of catching. the eroors and handling. them so the progam runs withou exiting

# they have 
 #1.Try block
 #2.except block
 #3.raise allows to us to rise our own errors
 #4.else block
 #5.finally block

#Try block
#This id the block where we write a code thats needs to be execupted
try:
    f=open("nkt.txt") #this file is not available in the system so it will throw an error

#except block:
#this block catches any error and returns withou causing the program to exit
except FileNotFoundError:
    print("File not found")#this throws an message that a file is not found 

#else block executes the next part of the code if no error is found
else:
    f.read()

#finally block runs iressecptive of the finds error or not this block is always ececuted
print("Program executing")

