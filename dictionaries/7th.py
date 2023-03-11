#Removing items from the dictionary
person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

#last items
p2=person.popitem()
print(p2)
print(person)

## Remove key 'telephone' from the dictionary
#p3=person.pop("weight")
#print(p3)

#del person['height']
#print(person)

#clear the dictionary
p4=person.clear()
print(p4)

del person
print(person)
