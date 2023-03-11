
tuple1 = (10, 20, 30, 40, 50, 60, 70, 80)
# Limit the search locations using start and end
# search only from location 4 to 6
# start = 4 and end = 6
# get index of item 60
var =tuple1.index(60, 2,8)
print(var)

#Checking if an item exists
print(30 in tuple1)
print(110 in tuple1)