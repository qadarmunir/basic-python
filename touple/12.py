#Copying a tuple
tuple1 = (10, 20, 30, 40, 50, 60, 70, 80,60,60,60 ,90, 100,60)
tuple1_copy = tuple1
print(tuple1_copy)
print(tuple1)

#append() method in tuple
simple_list =list(tuple1)
simple_list.append(200)
topuple3 =tuple(simple_list)
print(topuple3)
print(tuple1)