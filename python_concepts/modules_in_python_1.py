#this is the module tat should be imported and used 
#this returns the index of the arguments in the list
print("module impoeted")

test="test string:"

def f_index(to_find_from,target):
    for i,value in enumerate(to_find_from):
        if target==value:
            return i
    return -1

