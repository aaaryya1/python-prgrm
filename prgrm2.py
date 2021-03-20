start=int(input("enter current year:"))
end=int(input("enter the end year:"))
for i in range(start,end+1):
    if(i%4==0 and i%100!=0 or i%400==0):
        print(i)
    i=i+1

