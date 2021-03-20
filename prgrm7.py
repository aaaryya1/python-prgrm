list1=[12,4,6]
list2=[4,6,9,7,1]
l1=len(list1)
l2=len(list2)
sum1=0
sum2=0

#check length of 2 list is same or not

if l1==l2:
 print("length of both list are same")
else:
 print("length of both lists are not same")

#check length of 2 list is same or not

for i in list1:
 sum1=sum1+i
for j in list2:
 sum2=sum2+j
if sum1==sum2:
 print("sum of the lists is equal")
else:
 print("sum of 2 list is different")

#check wheather any value ocuur in both

for i in list1:
 for j in list2:
  if i==j:
   print(j,"occur in both list")