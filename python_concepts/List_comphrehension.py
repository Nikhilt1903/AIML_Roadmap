# List Comphreshensions
 #a list comphrehension is a short way to create lists using loops

# when to iuse list comphrehensiobs
#simple transformation
#filtering
#short logic

#we should avoid list comphresions
#complex logic
#too many nested loops
#hard to read

#for printing a square of numbers
squares=[i*i for i in range(1,5)]
print(squares)

#the basic syntax is 
#. [expression for item in iterable]

# =======================
#to unpack a list
nums=[1,2,3]

print(*[i*i for i in nums])

# ====================

# With condition(Filtering)
#syntax [expression for item in iterable if condition]

#for printing even numbers
even=[i for i in range(1,10) if i%2==0]
print(even)

# =========================

#with if else
# Syntax
#[expression_if_true if condition else expression_if false for item in iterable]

even_or_odd=[f"{i} is even" if i%2==0 else f"{i} is odd" for i in range(1,10)] 
print(even_or_odd)

# ===========================
#Nested list comphrehension
#syntax
# [expression for i in iterable for j in iterable]
app=[("*") for i in range(3) for j in range(3)]
print(app)

# ===========================
#flattening a list
matrix=[[1,2],[2,3],[3,4]]
flat=[j for i in matrix for j in i]
print(flat)

# ============================
#applying functions
def suqare_of(num):
    return num*num

num_sq=[3,6,9]
square_o= [suqare_of(i) for i in num_sq ]   
print(*[square_o])

# =============================
#string operations
name="Nikhil"
name_c=[i.upper() for i in name]
print(name_c)

# ===============================
#with enumerate

lst = ["a","b","c"]
enu=[(i,val) for i,val in enumerate(lst)]
print(enu)

# ================================
#with conditions
num=[1,2,3,4,5,6,7]
res=[i*i for i in num if i>3]
print(res)

# =================================
# dictionary comphrehension
nums = [1,2,3]
d = {i: i*i for i in nums}
print(d)

# ==================================
# set comprehension
s = {i*i for i in nums}
print(s)

# ==================================
