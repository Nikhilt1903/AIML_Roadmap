#Lists in Python
#lists are case sensitive
#List is structures
#lists and tupules allow us to work on sequential data
#Lists in python stores multiple values in a single variable
#list is mutable

#List is defined by: []

#example of a simple list:

courses=["Math","Science","History","Geography","CompSci"]

print(courses)
#working fine
print(courses.index("Science")) #gives the index of the item in the list
print("Science" in courses) #gives true if the item is present else returns false
print(len(courses)) #give the number of itesm in the list

print(courses[0]) #gives the first item in the list
print(courses[-1]) #gives the last item in the list

print(courses[0:4]) #gives the range of items from the list exluding the last item in the range
print(courses[:5]) #gives the range from 1st to the specified range
print(courses[2:]) #gives the range from specified start to the end 
#===================================================================================================

#List Operations
 #append
 #insert
 #extend
 #remove
 #pop. pop always returns the values that it popped
 #Reverse
 #sort
 #min
 #max
 #sum

num = [5,3,6,2,3]

print(courses)

courses.append("Data_Sci") #adds the element to the end of the list
courses.insert(0,"Intro") #add elemnt to the desired location

print(courses)


#if we want to add multiple values to a list we can do it by using extend
#this can be done by append and insert but these inserts the elemnts as a list but not imdivadual values

courses_2=["AIML","Cyber_sec"]
courses.append(courses_2) #adds course_2 as a entire list at the end of courses 
print(courses)

courses.insert(0,courses_2) #adds course_2 as a entire list at the especified location of courses 
print(courses)

courses.extend(courses_2) # adds course_2 as a individual items at the end of courses 
print(courses)

courses.remove("Data_Sci")#removes the specified element from the list
print(courses)

courses.remove(courses[0]) #removes the element at the specified position of the list
print(courses)

courses.pop() #removes the last e;lement of the list
print(courses)

popped=courses.pop() #pop returns the value of the removed element or item
print(popped)

courses.reverse()#reverses the list
print(courses)

courses.remove(courses[0])

sorted_courses = sorted(courses) #sorths the list in ascending order 
print(sorted_courses)

sorted_courses.reverse()#This gives the descending order
print(sorted_courses)

num.sort()#same like sorted() sorts the list in ascending order
print(num)

print(min(num)) #gives the minimum value
print(min(courses)) #gives the minimum vale

print(max(num)) #gives the maximum vale
print(max(courses)) #gives the maximum vale

print(sum(num)) #gives the sum of numbers in the list
# =====================================================================================

#Using loops in lists

list=["Hi","Bye","Good_bye"] 

for i in list:
    print(i)
#here it iterated throgh each item in the list and prints them

#using Enumerate in loops
#enumereate gives the index number along with the elements in the list
for index,i in enumerate(list):
    print(index,i)

#we can also specify the the start of the index in enumerate
for index,i in enumerate(list,start=1):
    print(index,i)

#turning our list into string by using
#Join
course_string=', '.join(courses) #this gives the comma sepaerated values of our list
print(course_string)

#turning a string back to a list
new_list=course_string.split(", ")
print(new_list)