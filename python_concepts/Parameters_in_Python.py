#A parameter is a variable that a function uses to receive input
#Parameter definition in python 
#inside a function we can assign default values to parameters
#so if dont give a value python will use default values

#***Default parameters must always come after non-default parameters.** else it causes a syntax error

#ex 
def greet(name):
    print("Hello",name)

greet("Nikhil")
#here name is the parameter, the function is expeccting a value for name
#we are calling the function greet passing nikhil as the argument or input

#"Nikhil" → argument (actual value passed)
#name → parameter (variable that receives it)

#example with multiple parameters
def add(a,b):
    print(a+b)

add(2,3)

#here we are defining a and b as parameters for function add and we are passing 2,3 as the arguments

def functi(a,b=5,c=10):
    print(a,b,c)

functi(5,c=20)

#here we are passing default arguments to parameters b and c
#if we dont pass any values to b and c it takes the default values
#if we dont pass any value to a it throes a error saying no argument for a 

