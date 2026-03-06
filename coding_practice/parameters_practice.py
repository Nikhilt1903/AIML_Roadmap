def add(a,b):
 print(a+b)

def multiply(a,b):
    print(a*b)

def is_even(n):
   if n%2==0:
      print("Even")
   else:
      print("Odd")

def largest(a,b):
   if a>b:
      print(f"{a} is largest")
   elif a==b:
      print(f"{a} and {b} is equal")
   else:
      print(f"{b} is largest") 

def power(base,exponent):
   print(base**exponent)

add(2,3)
multiply(6,9)
is_even(-4)
largest(99,99)     
power(2,6)