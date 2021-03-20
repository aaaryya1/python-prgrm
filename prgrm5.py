mlist=[]
n=int(input("enter the no of elements in the list: "))
for i in range(n):
 x=int(input("enter the no: "))
 if x<100:
   mlist.append(x)
 else:
  mlist.append("over")
print(mlist)
