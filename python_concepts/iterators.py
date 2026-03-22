# An iterator is an object that allows traversal of elements one ata a time using the next() functioin

#iterator does not give all values at once
#it gives one value ata time

# | Feature     | List       | Generator  | Iterator     |
# | ----------- | ---------- | ---------- | ------------ |
# | Memory      | High       | Low        | Low          |
# | Stores data | Yes        | No         | No           |
# | Reusable    | Yes        | No         | No           |
# | Indexing    | Yes        | No         | No           |
# | Ease of use | Easy       | Medium     | Hard         |
# | Use case    | Small data | Large data | Custom logic |

nums=[1,2,3]

it=iter(nums)

print(next(it))
print(next(it))
print(next(it))
# print(next(it))

#once it returns all the iterable values it throws stopiteration error

# iter() converts iterable to iterator
# next() gets next value

#using for loop in iterators

#normal code
nums=[10,20,30,40]

for n in nums:
    print(n)

#what actually happens internally

its =iter(nums)

while True:
    try:
        n=next(its)
        print(n)
    except StopIteration:
        break

#key understanding
# for loop=iterator + next + stopiteration

nums1=[1,2,3]

itsy=iter(nums1)

while True:
    try:
        b=next(itsy)
        print(b)
    except StopIteration:
        break

#Custom iterators

#we use custom iterators when we want full control over how iteration happens, instead of relying on built in data structures
#ex print only even numbers from 1-10
#when we dont want to store evrything we generate data on demand

#we use
#list  Normal Looping
#Generator Memory Efficiency
#Full control over iteration   Custom iterator

#Simple Counter

class COUNTER:
    def __init__(self, max):
        self.max=max
        self.current=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current<self.max:
            self.current+=1
            return self.current
        else:
            raise StopIteration
        
c=COUNTER(10)

for i in c:
    print(i)

#simple evn numbers only
class is_even:
    def __init__(self, max):
        self.max=max
        self.current=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current<self.max:
            self.current+=2
            return self.current
        else:
            raise StopIteration
        

        
w=is_even(12)

for i in w:
    print(i)

class reverse:
    def __init__(self,data):
        self.data=data
        self.index=len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index>0:
            self.index-=1
            return self.data[self.index]
        else:
            raise StopIteration
        
r=reverse(["nikhil","larthik"])

for i in r:
    print(i)
        