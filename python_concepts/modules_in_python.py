#learning how to import and work with modules
course=["math", "sci","bio","history"]

#when we import a module it runs the entire module so any print statements in the module will also run
import modules_in_python_1   #we use import statement 

index=modules_in_python_1.f_index(course,"sci") #we cannot use the functipnss from imported mosdule directly 
print(index)

import modules_in_python_1 as mp
ind=mp.f_index(course,"sci")
print(ind)

#we can also import specific functions from the module
#here we wont have acces to the entire module
from modules_in_python_1 import f_index as f
inde=f(course,"sci")
print(inde)

#to import evrything use *
#from modules_in_python_1 import *

#to check where pthon checks for the modules
import sys
print(sys.path)

# if we want import modles from other path we have to use
import sys
sys.path.append("pathe of the file")

#some random standard libraries
#random
#math
#calendar 
#os    