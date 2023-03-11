#Add multiple dictionaries inside a single dictionary
# each dictionary will store data of a single student
jessa = {'name': 'Jessa', 'state': 'Texas', 'city': 'Houston', 'marks': 75}
emma = {'name': 'Emma', 'state': 'Texas', 'city': 'Dallas', 'marks': 60}
kelly = {'name': 'Kelly', 'state': 'Texas', 'city': 'Austin', 'marks': 85}

class_six={"student1":jessa, "student2": emma, "student3": kelly}
print(class_six)

print(class_six['student1']["name"])
print(class_six["student1"]["marks"])

#Iterate through a dictionary
for key,value in class_six.items():
    print(key)
    print("\n")
    for key1,value1 in value.items():
        print(key1 ,":", value1)
        print("\n")