###Store your name, age, city in variables and print them.
name="Nikhil"
age=23
city="Bangalore"
out_mesage=f'Hi my name is {name} i am {age} years old. I stay in {city}'
print(out_mesage)
print(f'Hi my name is {name} i am {age} years old. I stay in {city}')
print(f""" Hi my name is {name} 
 i am {age} years old. 
 I stay in {city})""")

###Change age and print again.
name="Nikhil"
age=24
city="Bangalore"
out_mesage=f'Hi my name is {name} i am {age} years old. I stay in {city}'
print(out_mesage)
print(f'Hi my name is {name} i am {age} years old. I stay in {city}')
print(f""" Hi my name is {name} 
 i am {age} years old. 
 I stay in {city})""")

###Create 3 variables (a, b, c) and swap their values.
a=19
b="Nikhil"
c="hi"

print(a,b,c)
c=a
c=b
b=c

print(a,b,c)

# Print type of:
# an integer
# a float
# a string
# a boolean

print(type(15))
print(type(15.1))
print(type("Hi"))
print(type(True))