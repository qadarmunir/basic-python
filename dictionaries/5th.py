person = {"name": "Jessa", 'country': "USA", "telephone": 1178}

# update dictionary by adding 2 new keys
person["height"]=5.6
person.update({"weight":60})
print(person)

#another two methods to update a dictionary
person.update({"father":"John", "mother":"Mary"})
print(person)

person.update([("father","John"), ("mother","Mary")])
print(person)