#Using **kwargs to unpack
student_dict1 = {'Aadya': 1, 'Arul': 2, }
student_dict2 = {'Harry': 5, 'Olivia': 6}
student_dict3 = {'Nancy': 7, 'Perry': 9}
var={**student_dict1, **student_dict2, **student_dict3}
print(var)