#writing code using functions

#printing name using functions
def my_name():
    print("Nikhil")
    return "My name is Nikhil"
my_name()
print(my_name())

#Function for printing numbers from 1 to 10
def num_1_10():
    for i in range(1,11):
        print(i)

print(num_1_10())

#what happens in the num_1_10 function is after we define a function then it comes to the print statement, first it sees whats 
#inside the brackets that is num_1_10 so it prints 1_10 then it goes to thw print statement and prints none becausae there is no return statement 
# Defined in the function

#Print Multiplication table of 5
def mul_tab_5():
    for i in range(5,6):
        for j in range(1,11):
            print(i*j)

print(mul_tab_5())

