#Build Pattern
#*
#**
#***
#****

# n=4
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
    

#building reverse pattern
#****
#***
#**
#*

# n=4
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()

#printing muliplication grid

#printing a 3*3 grid
# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         # print("i=",i,"j=",j)
#         b=i*j
#         print(b,end=" ")
#     print()

#printing prime numbers agin
for i in range(2,51):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break

    if prime:
        print(f"{i} is a prime number")
    else:
        print(f"{i} is a composite number")    