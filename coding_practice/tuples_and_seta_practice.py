#practing coding basics for tupules

student=("Nikhil",23,"CSE") #creting a tupule for a student

print(student[0])
print(student[1])
print(student[2])

#looping throug tupule
for i in student:
    print(i)

print(len(student))

#tRYING TO MODIF A TUPULE
student[1]=25
# -------------------------------------------------------------------------------------------------

#Sets Practice

number_set={1,2,3,4,5,2,3} #duplicates will be auto removed
print(number_set)


number_set.add(7)
number_set.update([8,9,9,10])
print(number_set)

number_set.remove(8) #throws error if the item is not in the set
print(number_set)

number_set.discard(8)
print(number_set)

#union
number_set_1={1,3,6,12,15,18}
number_set_2=number_set.union(number_set_1)
number_set_3=number_set | number_set_1
print(number_set_2)
print(number_set_3)

#intersection
number_set_4=number_set.intersection(number_set_1)
number_set_5=number_set & number_set_1
print(number_set_4)
print(number_set_5)

#difference
number_set_6=number_set.difference(number_set_1)
number_set_7=number_set - number_set_1
print(number_set_6)
print(number_set_7)

num_set_8={1,2,3,4,5,7,9,10,11,13}
print(number_set.issubset(num_set_8))

print(num_set_8.issuperset(number_set))

