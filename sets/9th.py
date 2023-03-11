#Union of sets
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

new_set=color_set | remaining_colors
print(new_set)

#or we can use union method
set1= color_set.union(remaining_colors)

#Intersection of sets
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

#1st way
new_set=color_set & remaining_colors
print(new_set)

#2nd way
new_set=color_set.intersection(remaining_colors)
print(new_set)