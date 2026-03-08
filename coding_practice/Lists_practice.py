# #Basic lists practive

num=[1,3,4,5,6]
name=["NKT","KTN","NTN","MTB"]

#first element, last element ,second element
print(num) #prints the list of variabler num
print(name) #prints the list of variable name
print(num[0]) #prints the first element in num
print(name[0]) #prints the first element in name
print(num[-1]) #prints the last element in num
print(name[-1]) #prints the last element in name
print(num[1]) #prints the second element in num
print(name[1]) #Prints the second element in name

# # Write code that:

# # Creates a list of 5 numbers
# # Adds another number
# # Removes one number
# # Changes one value
# # Prints the length of the list


num_1=[]
elemen_num=int(input("Enter the number of elements to be entered"))

for i in range(elemen_num):
    elements=input("enter the element")
    i+=1
    num_1.append(elements)

print(f"this is the list {num_1}")

while True:


 print("""dO YOU WNAT TO PERFORM any of the below ooperations in the list?
1. ADD elements to the list
2. Remover elements from the lsit
3. modify elemnts in the list
4. print the length of the lust
5. Exit""")

 choice=int(input("eNTER YOU CHOICE FROM 1_5"))

 if choice==1:
     add_num=int(input("Enter the number of elements to be added"))
     for i in range(add_num):
         elements_add=input("enter the element")
         i+=1
         num_1.append(elements_add)
         print("the list ater append is ",num_1)

 elif choice==2:
    del_num=int(input("Enter the number of elements you want to remove"))
    for i in range(del_num):
         elements_del=input("enter the element")
         if elements_del in num_1:
             num_1.remove(elements_del)
             i+=1
             print("the list ater deleting is ",num_1)
         else:
             print("The number is not in the list")
            
 elif choice==3:
     index = int(input("Enter index to modify: "))
     new_value = input("Enter new value: ")
     if 0 <= index < len(num_1):
            num_1[index] = new_value
            print("Element updated.")
            print("the list ater updating is ",num_1)
     else:
            print("Invalid index.")

 elif choice==4:
     print(f"The length of the list is {len(num_1)}")

 elif choice==5:
     print(f"""The final list is
           {num_1}""")
     break
 else:
     print("invalid choice TRY AGAIN")


# list practice with loops
list_1=[1,2,3,45,46]
def all_el(lst):
    for i in lst:
        print(i)

def sqr(lst):
    for i in lst:
        print(i*i)

def eve_num(lst):
    for i in lst:
        if i%2==0:
            print(i)
    
def num_gre_5(lst): 
    lst_2=[]
    for i in lst:

        if i>5:
            lst_2.append(i)
    print(len(lst_2))


all_el(list_1)
sqr(list_1)
eve_num(list_1)
num_gre_5(list_1)

#Finding largest number in a list
list_3=[1,12,0,22,56,4]
largest=list_3[0]
for i in list_3:
    
    if i>largest:
        largest=i
print(largest)

#Removing Duplicates
list_4=[1, 2, 2, 3, 4, 4]
list_5=[]
for i in list_4:
    if i not in list_5:
        list_5.append(i)
print(list_5)

#grequency counter
lst_6 = [1,1,2,3,3,3]

for i in set(lst_6):
    print(i, "=", lst_6.count(i), "times")