list=[]
n=int(input("enter the number of words in the list:"))
for i in range(n):
 x=input("enter the word:")
 list.append(x)
print(list)
length=len(list[0])
temp=list[0]
for i in list:
 if len(i) > length:
  length=len(i)
  temp=i
print("the longest word is of length",length)