import csv

header = ["place", "name", "age"]
with open("city.csv", "w") as file:
    write = csv.DictWriter(file, fieldnames=header)
    write.writeheader()
    write.writerow({"place": "malaparamba", "name": "aarya", "age": 21})
    write.writerow({"place": "civil", "name": "Anjana", "age": 21})
    write.writerow({"place": "vatakara", "name": "chithra", "age": 23})
    write.writerow({"place": "payyoli", "name": "anuuu", "age": 13})
with open("city.csv", "r") as file:
    read = csv.DictReader(file);
    n = input("Enter the column name you want(place,name,age):")
    for i in read:
        print(i[n])