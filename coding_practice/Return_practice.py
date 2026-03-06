def square(a):
    return a*a

def factorial(b):
    total=1
    for i in range(1,b+1):
        total=total*i
    return total

def prime_checker(n):
        is_prime=True
        for j in range(2,n):
            if n%j==0:
                is_prime=False
                break
        if is_prime==True:
             return f"{n} is prime"
        else:
             return f"{n} is composite"
            

num=int(input("enter the number to find the square,factorial and whether its prime or composite"))
print(f"the square of {num} is {square(num)}")
print(f"the factorial of {num} is {factorial(num)}")
print(prime_checker(num))


def are_circle(radius):
     return 3.1459*radius*radius

rad=int(input("Enter the radius of the circle"))
print(f"The are of the circle is {are_circle(rad)}")

def sum_n_numb(n=7):
     sum=0
     for i in range(1,n+1):
          sum=sum+i
     return sum

su=int(input("Enter the number for which you need the sum"))
print(f"the sum is {sum_n_numb(su)}")