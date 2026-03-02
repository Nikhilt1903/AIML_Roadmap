#if,id-else,if-else-if

#IF
language="Python"
if language=="Python":
    print("You are using python")

#IF_ELSE
language="Python"
if language=="Python":
    print("You are using python")
else:
    print("You are using java")

#if_else_if
language="Python"
if language=="Python":
    print("You are using python")
elif language=="Java":
    print("You are using Java")
else:
    print("you are using C")

#using if and boolean
user="Admin"
logged_in=True
if user=="Admin" and (logged_in):
    print("Login Successfull")
else:
    print("Login Failed")

#using if and not with boolen
user="Admin"
logged_in=True
if user=="Admin" and not(logged_in):
    print("Login Successfull")
else:
    print("Login Failed")