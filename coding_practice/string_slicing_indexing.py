word="Programming"
print(word[0])
print(word[2])
print(word[-1])

x=input("Enter the sentence")

print(len(x))
print(x)
print(x.upper())
y=x.replace("name","names")
print(y)

#bASIC LOOP IN PYTHOMN

for i in x:
    print(i)

#counting vowels in python
vowels=0
consonants=0
spaces=0
for i in x:
    if i==" ":
        spaces+=1
    elif i in "aeiouAEIOU":
        vowels+=1
    else:
        consonants+=1
        

print(f"the num,ber of vowels in the word is {vowels}")
print(f"the num,ber of consonants in the word is {consonants}")
print(f"the num,ber of spaces in the word is {spaces}")

#Reversing a string
y=x[::-1]
print(y)

#or
revers=""
for i in x:
    revers=i+revers
print(revers)

#palindrome checker
if x==y:
    print("the string is a palindrome")
else:
    print("Npt a palimdrome")

#word counter
z=x.split()
print(len(z))