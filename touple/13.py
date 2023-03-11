#Concatenating two Tuples
#Using the + operator
touple1 = (1,2,3,4,5,6,7,8,9,10)
touple2 = (11,12,13,14,15,16,17,18,19,20)
tuple3= touple1 + touple2
print(tuple3)

#using sum keyword
touple1 = (1,2,3,4,5,6,7,8,9,10)
touple2 = (11,12,13,14,15,16,17,18,19,20)
touple3 =sum((touple1 , touple2), ())
print(touple3)

#Using the chain() function
import itertools
touple3 =tuple(item for item in itertools.chain(touple1, touple2), ())
print(touple3)