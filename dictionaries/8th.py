#Checking if a key exists
person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}
key_value= "weight"
if key_value in person:
    print("weight is :", person[key_value])
else:
    print("weight is not found")

    #Join two dictionary
    person2 = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}
    person3= {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}
    person2.update(person3)
    print(person2)