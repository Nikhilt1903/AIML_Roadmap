#extract only vowels
vowels="aeiou"
srring=["karthik"]
vow_yes=[j for i in srring for j in i if j in vowels]
print(vow_yes)


#latten nested list
a=[[[1,2],[3]],[[4,5]]]
flatte=[k for i in a for j in i for k in j]
print(flatte)

#replacing even numbers with even
eve=[1,2,3,4]
num_is_e=["even" if i%2==0 else i for i in eve]
print(num_is_e)

#created dictionary using comhresiom for cubes
dic={i:i**3 for i in range(1,4)}
print(dic)

#numbers divisible by 3 and 5 from 1-100
print(*[i for i in range(1,101) if i%3==0 and i%5==0])

#length of each word in a list
lst=["hi","nikhil","laru"]
print(*[len(i) for i in lst])

#reverse every tring ina lsit
print(*[i[::-1] for i in lst])

#multiflication table for 5
print(*[i*j for i in range(5,6) for j in range(1,11)])

# Generating a lsit of squares from 1-20
squares=[i*i for i in range(1,21)]
print(squares)

#get all odd numbers from 1-20
odd=[i for i in range(1,21) if i%2!=0]
print(odd)

#convert list of strings to upper case
list_s=["nikhil","karthik","men"]
caps=[i.upper() for i in list_s]
print(caps)

#flattening a nested list
list_f=[["nkt",1,"ka"],["a",3,4]]
pri=[j for i in list_f for j in i]
print(pri)

# replace neagative numbers with 0
list_n=[-1,-2,3,6,-7,12]
prin=[0 if i<0 else i for i in list_n ]
print(prin)


#counting digits in list of strings
lis_1=["a1","b22","c333"]
numbers="1234567890"
digi=[j for i in lis_1 for j in i if j in numbers]
i=set(digi)
j=list(i)
print(j)

#flatten and square
a=[[[1,2],[3]],[[4,5]]]
flatte=[k*k for i in a for j in i for k in j]
print(flatte)

#swap case
#we also have .swapcase() option in python
name="NikHiL"
print(*[i.upper() if i==i.lower() else i.lower() for i in name])