#Copying a list
list1=["qadar", "ali", 1, 2]
print(list1)
list2=list1    #using operator
list2.append("qadar")
print(list2)

#use copy method
list3=list2.copy()
list2.append("ali")
print(list3)
print(list2)