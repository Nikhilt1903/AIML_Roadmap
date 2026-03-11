#A tupule in python is a immutable datatype
#the data inside a tupu;e cannot be modified once it is created
#Tupules are represented by ()
#Tupules are always used by comma seperated values

#ex of not a tupule
x=(1)
print(type(x))

#ex of a tupule
y=(1,)
print(type(y)) #this gives a tupule because its seperated by commas+

#Tupules are faster
#tupules are memory efficient
#tuples are safe from modification 
#tupules are hashable that is it can be used as keys for dictiopnaries

#tupules also help unpacking multiple values at once
a,b,c=(1,2,3)
print(a)
print(b)
print(c)