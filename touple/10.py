#Removing items from a tuple
# there are two methods of deleting items from a tuple
# 1_ using del keyword
#converting a tuple to a list

#touple1 = (1,2,3,4,5,6,7,8,9,10)
#del touple1
#print(touple1)

#By converting it into a List
touple1 = (1,2,3,4,5,6,7,8,9,10)
simple_list =list(touple1)
simple_list.remove(5)
toupple2= tuple(simple_list)
print(toupple2)
