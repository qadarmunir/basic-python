#nested dictionary
# address dictionary to store person address
address = {"state": "Texas", 'city': 'Houston'}

# dictionary to store person details with address as a nested dictionary
person = {'name': 'Jessa', 'company': 'Google', 'address': address}
print(person)

print("address is :",person['address']['city'])

#nested loop in dictionary
for key ,item in person:
    if key=="address":
        print("address  is :")
        for key1,value1 in values.items():
            print(key1,":",value1)
    else:
        print(keys, ":", values)