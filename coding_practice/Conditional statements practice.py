#even or odd
print("Even or odd calculator")
x=int(input("""Enter a number to check if its even or odd
"""))
if x%2==0:
    print("The number is even")
else:
    print("The number is odd")

#positive negative or zer0

print("Positive negative or zero checker")
y=float(input(""" Enter a Number
   """))
if y>0:
    print(f"round{y} is positive")
elif y<0:
    print(f"{y} is negative")
else:
    print(f"{y} is a zeroooo")

#Grade calculator (A/B/C/F)

print("GRADE CALCULATOR")
z=int(input("""Enter the marks of the student
"""))
if z>=85:
    print("A Grade")
elif z>=60:
    print("B Grade")
elif z>=40:
    print("C Grade")
else:
    print("Fail")

#Leap year checker
l=int(input("""Enter the year you wnat to check whether its leap year or not
"""))
if l<0:
    print("Years cant be negative please enter a postive vallue")
elif (l%400==0 or l%4==0) and (l%100!=0):
    print("Its a leap year")
else:
    print("its not a lep year")