#Printing 1-0 usin both for and while lopp

#Using for loop
for i in range(1,11):
    print(i)

#using while loop
i=1
while i<11:
    print(i)
    i+=1

#sum of first n numbers using for and while
n=int(input("Enter the number to calculate the sum of number"))
total=0
for i in range(1,n+1):
    total=total+i    
print(total)
         
#using whie loop
n=int(input("Enter the number to calculate the sum of number"))
i=0
total=0
while i<=n:
    total=total+i
    i+=1
print(total)

#Multiplication table using for and while
#using for
n=int(input("Enter the number for which you need the multiplication table"))
y=int(input("Emter the number till where you need the multiplied table"))

for i in range(1,y+1):
    multply=n*i
    print(f'{n}*{i}={multply}')


