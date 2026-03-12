#basic coding practice for exception handling

print("Program for dividing two numbers")

try:
    num_one=int(input("Enter the first number"))
    num_two=int(input("enter the second number"))

    answer=num_one/num_two
    
except ValueError : #as e:
    #print(e)
    print("enter a number not a string!")

except ZeroDivisionError:
    print("The number cannot be divided by 0")

else:
    print(answer)

finally:
    print("You write whatever you want i will be running.....")


#or..................
try:
    num_one = int(input("Enter the first number: "))
    num_two = int(input("Enter the second number: "))

    answer = num_one / num_two

except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

else:
    print(answer)

finally:
    print("Program finished")


#exapmpe with raise
print("Program to withdraw money")

balance = 5000

try:
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        raise ValueError("Insufficient balance")

except ValueError as e:
    print("Error:", e)

else:
    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)

finally:
    print("Transaction completed")