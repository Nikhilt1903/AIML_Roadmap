# a set is a mutable data stt=ructure
#a set is uesd in case of duplicates that is set foes not allow duplicates
#a stores unorderd collection of data
#a set is reresented by {}
#sets cant be indexed as they are unorderd

#sets are commonly used for
#removing duplicates
#membership teting
#comaprig collections
#mathematical set operations

sets={} #this creates a empty dictionary

sets_1=set() #this creates a empty set

sets_2={"Nikhil","karthik"}
print(sets_2)

print("Nikhil" in sets_2) #returns true or false

sets_2.add("Hi") #adds a element to the set
print(sets_2)

sets_2.update(["bye","conjo"])# to add multiple elements
print(sets_2)

sets_2.remove("conjo") #removes the element but throws error if its not in the set

sets_2.discard("conjo") #no error if element is not present
print(sets_2)

sets_2={"Nikhil","karthik","Nikhil","boys"} #it does not support duplicates
print(sets_2)

sets_3={"boy","boys"}

#union combines two sets removing the duplicates unionn or |
sets_4=sets_2.union(sets_3)
print(sets_4)

#intersection gives the elements present in both set_2 and set_3 intersection or &
sets_5=sets_2.intersection(sets_3)
print(sets_5)

#difference gives the elements that are there in set 2 but not in set 3 difference or -
sets_6=sets_2.difference(sets_3)
print(sets_6)

#symetric_difference
#This gives the uncommon elemts in both the sets 
A = {1,2,3}
B = {3,4,5}

print(A.symmetric_difference(B))

#intersection_update()
#this provides the common elemts and updayes the set with the common ele
C = {1,2,3,4}
D = {3,4,5}

C.intersection_update(D)
print(C)

#difference_update()
E = {1,2,3,4}
F = {2,4}

E.difference_update(F)

print(E)