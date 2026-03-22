#genertaor with loop
def count(n):
    for i in range(1,n+1):
        yield i

for num in count(5):
    print(num)


#square generator
def squares(n):
    for i in range(1,n+1):
        yield i*i

for i in squares(6):
    print(i)

#even generator
def eve_gen(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i

for i in eve_gen(6):
    print(i)


#countdpwn gen
# def countdo(n):
#     for i in range(n+1,0,-1):
#         yield i

def countdo(n):
    while n > 0:
        yield n
        n -= 1

for i in countdo(5):
    print(i)