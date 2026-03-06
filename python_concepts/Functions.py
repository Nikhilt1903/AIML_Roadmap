#Functions are used to perform a specific task in python
#insteding of typing the code again and again we can store it in a function and call it whenever needed
#def is used to define a function
#when we pass *args,**kwargs its takes them as key value pairs

# #Example
def hello_function():
    pass #just an example we use "pass" to run the code without an error as we did not return anything it the functions

hello_function()


#simple way to print a function
def hello_func():
    print("Hello Function")

hello_func()

# #calling fuction inside a loop
for i in range(0,4):
    print(hello_func())

#Return value in a functtion
#return values states what should be written when we run a function, so when we use print without defuing a return in a finction it prints None
#when we return something in the function and use it in print it returns the value used

#example
#without using return
def hello_func():
    print("Hello Function")

print(hello_func())

#using return
#it returns "Hello function" when a function is called with print 
def hello_funct():
    print("Hello Function")
    return "Hello Function"

print(hello_funct())

def fnc_args(*args,**kwargs):
    print(args)
    print(kwargs)

fnc_args("name","age",name="Nihil",age=22)