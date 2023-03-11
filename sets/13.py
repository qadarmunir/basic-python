#nested set
rainbow = ('violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red')
other_colors = ('white', 'black', 'pink')
new_set=((frozenset(rainbow),frozenset(other_colors)))
for i in new_set:
    print(i)

    #set comprisition
    square_set={var**2 for var in range(1,11) if var%2==0}
    print(square_set)