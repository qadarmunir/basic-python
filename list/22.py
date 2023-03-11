#List Comprehension
#List comprehension is an elegant way to define and create lists based on existing lists.
list1=[1,2,3,4,5,6,7,8,9,10]
list2 =[var**2 for var in list1 if var%2==0]
print(list2)

#2nd exapmle
list3=[var**2 for var in range(10) if var%2==0]
print(list3)