#Simple way to open. afile

#open command helps to specify whether we are opening the file for reading,writing,appending,or reading and writinh
#if we do not specify anything it opens the file in reading mode
# "r" for reading a file
# "w" for writing a file
# "a" for appending a file
# "r+" for reding and writing a file
# "rb" for writing in binary mode
# "wb" for writing in binary mode

##without context manager
f=open("/Users/nikhil/coding/AIML_Roadmap/python_concepts/test.txt","r")
print(f.name)
print(f.mode)
f.close()

#With context manager
#we use context manager because whenever we open a file we should close the file mandotarily 
#if we forget to cloose it stores all the data in the file 

#in order to over come thos we use the context manager as it closes the file automatically
with open("/Users/nikhil/coding/AIML_Roadmap/python_concepts/test.txt","r") as f:
    pass

print(f.closed) #here it returs true beacuse the file is closed automaticaaly


#printing the contents of the file
with open("/Users/nikhil/coding/AIML_Roadmap/python_concepts/test.txt","r") as f:
    f_contents=f.read()
    print(f_contents)
    f_contents=f.readlines() #it conversts all the lines in the file to a list
    print(f_contents)
    f_contents=f.readline() #f.readline only prints the single line everytime it runs
    print(f_contents)

# so these are fine if we have small amout of data in a file to read what if we have a large data and want the control on
# what to read from the file

#we can specify the number of characters to be read within the read function
with open("/Users/nikhil/coding/AIML_Roadmap/python_concepts/test.txt","r") as f:
    f_contents=f.read(100) #this prints the first 100 characters in our file
    print(f_contents,end="")

    f_contents=f.read(100) #when we run this again this prints the next hundred characters starting from where it left
    print(f_contents,end="")

    f_contents=f.read(100)
    print(f_contents)

#we can use f.tell() to see the current position of the file
#we can use the f.seek() to manipulate the position in the file
# -------------------------------------------------------------------------------------------------------

#Writing into a file
with open("test_2.txt","w") as f:
    f.write("test")
    f.write("test")
    f.seek(0)
    f.write("test")

# ----------------------------------------------------------------------------------------------------------
#reading and writing into a text file
with open("/Users/nikhil/coding/AIML_Roadmap/python_concepts/test.txt","r") as rf:
    with open("test_copy.txt","w") as wf:
        for line in rf:
            wf.write(line)

# ----------------------------------------------------------------------------------------------------------
# for reading and writing a jpeg file we should read and writ e them in binary mode
with open("/Users/nikhil/Desktop/Photos and sign/photo.JPG","rb") as rf:
    with open("test_copy.jpg","wb") as wf:
        for line in rf:
            wf.write(line)