#Copy a Dictionary
dict1={"name":"qadar", "country":"pak", "age":13}
dict2=dict1.copy()
print(dict2)

#anther way to copy a dictionary
dict3=dict(dict1)
print(dict3)

#Copy using the assignment operator
dict4=dict1
print(dict4)
dict5=dict4.update("age":25)
print(dict5)
print(dict4)