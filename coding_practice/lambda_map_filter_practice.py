#cube of all numbers using map
nums=[1,2,3,4,5]
res=list(map(lambda x:x**3,nums))
print(res)

#filter numbers>10
num=[10,20,9,25,11,6]
res_1=list(filter(lambda x:x>=10,num))
print(res_1)

#add two lists using mapp
res_2=list(map(lambda x,y:x+y,num,nums))
print(res_2)

#remove empty strings using filter
stri=["nkbg","","kfffkt","","hav"]
res_3=list(filter(lambda x:x!= "",stri))
print(res_3)

#sort dictionary by values
d={1:2,2:3,4:5,3:1}
res_4=dict(sorted(d.items(),key=lambda x:x[1]))
print(res_4)

#double only even numbers
res_5=list(map(lambda x:x**2,filter(lambda x:x%2==0,nums)))
print(res_5)

#convert words to uppercase using map
res_6=list(map(lambda x:x.upper(),stri))
print(res_6)

#filter words with length > 3
res_7=list()