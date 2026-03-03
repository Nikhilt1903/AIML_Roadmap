#understand nested loops properly

#A Loop Inside a Loop is called a nested loop
#so the main concept is
#1.Outer loop controls rows and inner loops controls columns
#2,total iterations=outer*inner

for i in range(1, 4):#outer loop
    for j in range(1, 4):#inner loop
        print("i =", i, "j =", j)
#What this does is outer loop gives i as input the inner loop gives j as input
#it maps with i,j till inner loop is complete

##the inner loop is used for number of turns it iterates