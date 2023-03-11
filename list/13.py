#Remove specific item
#remove(object)
list1=[10, 20, 'Jessa', 12.50, 'Emma', 25, 50]
list1.remove(20)
print(list1)

list1.remove("Emma")
print(list1)


#remove same items using  loop
list2=list([10, 20,50,50, 'Jessa', 12.50, 'Emma', 25, 50])
for i in list2:
    #if i==50:
    list2.remove(i)
print(list2)    