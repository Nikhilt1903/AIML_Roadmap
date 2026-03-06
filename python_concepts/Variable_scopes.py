#scopes is defined by LEGB
#L:LOCAL
#E:ENCLOSING
#G:GLOBAL
#B:BUILT_IN

#Python always follows LEGB Rule

x="Global X"

def fun():
    y="local y"
    print(y)

fun()
print(x)

#what happens above is x is defined outside the function so its global
#y is define inside a function so its local
#so it prints local y and global x

# ****#Now ltes replace print(x) with print(y)
x="Global X"

def fun():
    y="local y"
    print(y)

fun()
print(y)
#nOW The one throws an error because y is define locally inside the function fun()
#so when we call it outside the function it doesnt recognize it and throws an error

# ***** now lets replace the print(y) inside the fun() to print(x)
x="Global X"

def fun():
    y="local y"
    print(x)
fun()
print(x)
#this runs without an error although its not defined inside the function because its declared globally

# ***** Now lets declare y as global inside the function using global keyword
#x="Global X"

def fun():
    global y
    y="local y"
    print(y)

fun()
print(y)
#This runs without an error because we are defiing y globally so if it runs even if we call it outside the function as well

# **** Now lets define y as global insude the fun() and agin replace it with another value
y="Global Y"

def fun():
    global y
    print(y)
    y="local y"

fun()
print(y)
#what happens here is it runs the fun() see print(y) and prints the globaly
#Then we are rplaceing the vale of teh the variable y to local y now y is initialize to local y
#there it prints localy y even when its called outside the function

