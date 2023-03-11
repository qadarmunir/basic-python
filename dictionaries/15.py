#Dictionary comprehension
n={2,4,6,8}
square= {x:x**2 for x in n if x % 2==0}
print(square)

telephone_book = [1178, 4020, 5786]
persons = ['Jessa', 'Emma', 'Kelly']
data= {key:value for key,value in zip(persons, telephone_book)}
print(data)
