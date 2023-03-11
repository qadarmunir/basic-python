#modifying the list
my_list = list([2, 4, 6, 8, 10, 12])
#single element
my_list[2]=100
print(my_list)

# modify range of items
# modify from 1st index to 4th
my_list1 = list([2, 4, 6, 8, 10, 12])
my_list1[1:3]=[100,200,300]
print(my_list1)

#modify from 3rd index to end
my_list2 = list([2, 4, 6, 8, 10, 12])
my_list2[3:]=[300,400,500,600]
print(my_list2)