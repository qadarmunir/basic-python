#Removing item(s) from a set
color_set = {'red', 'orange', 'yellow', 'white', 'black'}

#remove an item
color_set.remove('white')
print(color_set)

#discord an item
color_set.discard('black')
print(color_set)

#pop , in which we can remove random item
color_set.pop()
print(color_set)

#clear, in which we can remove all items
set1={"Harry Potter", "Angels and Demons", "Atlas Shrugged"}
set1.clear()
print(set1)

#delete, in which we can delete the set
set1={"Harry Potter", "Angels and Demons", "Atlas Shrugged"}
del set1
print(set1)