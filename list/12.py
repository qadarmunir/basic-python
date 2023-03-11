#Modify all items
list1=[10, 20, 'Jessa', 12.50, 'Emma', 25, 50]
for i in range(len(list1)):
    square= list1[i] * list1[i]
    list1[i]=square
print(list1[i])