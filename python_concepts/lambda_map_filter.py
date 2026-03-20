# lambda creates a small functions quickly
#map() apply functon to all items
#filter() pic items based on condition

# Use Case	Best Choice
# Simple transformation	list comprehension
# Simple filtering	list comprehension
# Complex pipeline	map/filter
# Sorting	lambda
# Short function	lambda

# =======
#lambda
#we use lambda to vreate a quick one line functions without formally defining theem using def
#syntax = lamba arguents:expression

#has only one expression 
# no return value
# no statements like loops and assignments

#example

square=lambda x:x*x
print(square(4))

is_even=lambda x:x%2==0
print(is_even(5))

# ==========
#map
#map is used to apply function to all elements
#syntax= map(function,variable)

nums=[1,2,3,4,5]
result=list(map(lambda x:x*x,nums))
print(result)

# ============== 
#filter
#we use filter to filter the elements based on condition
#synax=filter(funr=ction,iterable)

res=list(filter(lambda x:x%2==0, nums))
print(res)

# maps() tranforms the vlaues and filter only selects the filteres val;ues