#Use ctrl+c to come out of infinite loop


#for loops and while loops
#we use for loops when a number of iterations is known
#we use while loops when we dont know thw number of iterations ex boolean conditions

#Break and continue in loops

#break: it completely breaks  the loop once the condition is satisfied
# nums=[1,2,3,4,5]
# for num in nums:
#     if num==3:
#         print("found")
#         break
#     print(num)

#continue: it still continues to excecute the loop even the statement is satisfired
# nums=[1,2,3,4,5]
# for num in nums:
#     if num==3:
#         print("found")
#         continue
#     print(num)

#loop within a loop

# nums=[1,2,3,4,5]
# for num in nums:
#     for letter in "abc":
#         print(num,letter)

#range
#prints numbers from 0 to 5
# for i in range(6):
#     print(i)

#prints numbers from 1 to 5
# for i in range(1,6):
#     print(i)

#while loop
#its based on the conditions 
# i=0
# while i<5:
#     print(i)
#     i+=1

#using while for infinite loop

i=0
while True:
    print(i)
    i+=1