#Arithematic ops:
#addition: 3+2
#sub: 3-2
#mul:3*2
#divide: 3/2
#floor div: 3//2
#exponent(square): 3**2
#modulus 3%2

print(3+2) #add
print(3-2) #subract
print(3*2) #multiply
print(3/2) #divide
print(3//2) #divides and reedues to nearest integer doe not give decimal values
print(3**3) #powers
print(3%2) #reminders

print(3*2+1) #uses bodmas automatically
print(3*(2+1)) #uses bodmas

#increment
num=1
num=num+1
print(num)

#increment
num=1
num +=1
print(num)

num *=10
print(num)

print(abs(-1)) #abs always returs positive values
print(round(3.75,1)) #round

#Comparison opertaors
#Equal: 3==2
#not equal: 3!=2
#greater than: 3>2
#less than: 3<2
#greater or equal: 3>=2
#less or equal: 3<=2

num_1=3
num_2=2

print(num_1==num_2)
print(num_1>num_2)
print(num_1<num_2)
print(num_1!=num_2)
print(num_1>=num_2)
print(num_1<=num_2)

#to convert textual data into integers just use
#num_1=int(num_1)

x=5
print(id(5))
x=x+1
print(id(x))