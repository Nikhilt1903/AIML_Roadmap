#practicing file handling reading writing to a file

with open("dta.txt","w") as f:
    f.write("Hello world")

with open("dta.txt","a") as f:
    f.write("Hello world")

with open("dta.txt","r") as r:
    print(r.read())

#asking for the user name and saving it to the file

name=input("enter your name")

with open("dta.txt","a") as na:
    na.write(name+"\n")

#writing a program for everyday expense tracker
# while True:
#     x=int(input("""click 
#         1 to enter a exnse
#         2 to exit"""))
#     if x==1:
#         y=input("""Enter the expense
#                 """)
#         with open("expense_tracker.txt","a") as w:
#             w.write(y+"\n")
#     else:
#         print("Exiting the loop")
#         break


print("Welcome to the expense tracker")
expense={}
while True:
    x=int(input("""click 
        1 to enter a exnse
        2 to exit"""))
    if x==1:
        date=input("Enter the date in yyyy-mm-dd format")
        item=input("Enter the type of expense")
        amount=int(input("Enter the amount spent"))
        
        if date not in expense:
            expense[date]={}
            expense[date][type]=amount
            with open("expense_tracker_1","a") as r:
                r.write(f"{date}: {item} {amount}\n")
        else:

            expense[date][type]=amount
            with open("expense_tracker_1","a") as r:
                r.write(f"{item} {amount}\n")

    else:
        print("exiting the loop")
        break
