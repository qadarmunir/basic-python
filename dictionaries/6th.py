#Set default value to a key
dict1={"name":"qadar", "country":"pak", "age":13}
dict1.setdefault("city", "sargodha")
dict1.setdefault("country", "USA")
for keys,items in dict1.items():
    print(keys, ":", items)