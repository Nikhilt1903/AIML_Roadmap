#Return is used to send a value back from a function
#without return, a function returns none

# ****The function will not run further after a return statement thei anything after return will not be preocesed

#example without return
def add(a,b):
    print(a+b)

result=add(3,4)
print(result)
#Here the output will be 7 none because it stores a function add then it comes to result where we have give add(3,4) so its runs the functiom and prints 7
#but there is not return value so it store result =none and prints none

#example with returmn
def add(a,b):
    return a+b

result=add(3,4)
print(result)

# Parameter is a variable inside a function 
# argument is a valuue passed to a parameter
# return sends value back from Function
# print just displays value

def test(a):
    return a * 2

print(test(5) + 3)

#This prints 13 beacuse
#1. def test(a) is creates a function named test with parameter a. Nothing runs yet.
#2.test(5) it runs a function test and reti=urs 10 and stores the value 10
#3.then python evaluates 10+3 and gives 13

def demo(x):
    print(x * 2)
    return x + 1

print(demo(4))
#This will print 8 and 5
#here print dispalys immediately when the funcytion runs 
#return sends a value back when the function is ca;l;ed

def test():
    print("Hello")
    return
    print("World")

test()

#Here first it runs test and prints hello then returns
#anything after return will not be processed so world will never be prined 
#the output will be onlr Hello

def fun():
    print("A")
    return 3
    print("B")

print(fun() + 2)

# first it will define a function fun() then it reaches fun() inside print 
# so it prints a A 
# then it goes to print which uses a return value that is 3+2 and returns 5 
# so the final output will be A 5