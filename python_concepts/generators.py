# []=list comphrehension
# ()=generators
#A generator is a function that useing yeild instead of return
#it produces values one ata atime not all at once

# | Feature     | List       | Generator  | Iterator     |
# | ----------- | ---------- | ---------- | ------------ |
# | Memory      | High       | Low        | Low          |
# | Stores data | Yes        | No         | No           |
# | Reusable    | Yes        | No         | No           |
# | Indexing    | Yes        | No         | No           |
# | Ease of use | Easy       | Medium     | Hard         |
# | Use case    | Small data | Large data | Custom logic |

# | Situation            | Use       |
# | -------------------- | --------- |
# | Small data           | List      |
# | Large data           | Generator |
# | File processing      | Generator |
# | Pipelines            | Generator |
# | Infinite sequence    | Generator |
# | Need indexing        | List      |
# | Reuse multiple times | List      |
# | Custom logic         | Iterator  |



#we use list when we need to acces data again and need indexing 

#we use generators for memory efficient and on demand processing

## a generator is a memory efficin=ent iterator that produces values lazily using the yeild keyword


# “Lists are used when we need full data access and reuse. Generators are used for memory-efficient, 
# on-demand processing. Iterators are used when we need custom control over iteration.”

#example 
def gen():
    yield 1
    yield 2
    yield 3

g= gen()

print(next(g))
print(next(g))
print(next(g))

for i in g:
    print(i)

# yeild pauses the fumction, then when we next() it resumes from where it stopped 