#Print numbers 1–20
# for i in range(1,21):
#     print(i)

#print even numbers from 1-50
# for i in range(1,51):
#     if i%2==0:
#         print(i)

#Multiplication table of 7
# for i in range(1,11):
#     i=i*7
#     print(i)

#Sum of first N numbers
# n=int(input("Enter the value to find the sum"))
# num=0
# sum=0
# while num<=n:
#     sum=sum+num
#     num+=1
# print(sum)

#factorial using loop
# n=int(input("Enter the value to find the fcatorial"))
# for i in range(n,1):
#     facto=n*i
#     print(facto)

# n=int(input("Enter the value to find the fcatorial"))
# num=1
# facto=1
# while num<=n:

#     facto=facto*num
#     num+=1
# print(facto)

# n=int(input("Enter the value to find the fcatorial"))
# facto=1
# for i in range(1,n+1):
#     facto*=i
#     print(facto)

#Print prime numbers from 1–50
for i in range(2, 51):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i)
  
#reversal of number
n=int(input("Enter the value to reverse"))
reverse=0
while n>0:
    number=n%10
    reverse=reverse*10+number
    n=n//10
print(f"The number is {reverse}")

