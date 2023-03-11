#we cannot add value directly in touple  if we add value in touple then we will get error
tuple1=(1,2,3,4,5,6,7,8,9,10)
#touple[1]=11
#print(tuple1)
 #first we convert touple into list then we add value in list then we convert list into touple
simple_list=list(tuple1)
simple_list.append(11)
new_touple=tuple(simple_list)
print(new_touple)