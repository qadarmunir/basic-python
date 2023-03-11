#difference
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

#1st way
new_set=color_set - remaining_colors
print(new_set)

#2nd way
color_set.difference_update(remaining_colors)
print(color_set)


#symmetric difference
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
set3=color_set ^ remaining_colors
print(set3)

#or we can use symmetric_difference method
color_set1 = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
s2=color_set1.symmetric_difference_update(remaining_colors)
print(s2)