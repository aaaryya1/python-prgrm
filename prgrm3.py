#list comprehension
#a.generate positive list of nos from a given list of integers

list=[1,-3,2,4,-6,3,-5,-9,-10]
newlist=[x for x in list if x>0]
print(newlist)

#b.square of N nos

mlist=[]
n=int(input("enter the number of nos:"))
for i in range(n):
 x=int(input ("enter the number "))
 mlist.append(x)
for i in range(n):
 newl=[x**2 for x in mlist]
print(newl)

#form a list of vowels

word="aarya"
vowel=['a','e','i','o','u']
for i in range(len(word)+1):
 newl=[x for x in vowel if x in word]
print(newl)

#list of ordinal values
word="apple"
mlist=[ord(x) for x in word]
print(mlist)
