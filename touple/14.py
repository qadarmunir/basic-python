#Nested tuples
nested_tuples=((1,2,3,4,5),(4,5,6,7,8),(9,10,11,12,13),"python") 
print(nested_tuples[1][0])

#looping 
for i in nested_tuples:
    print("tuple", i, "elements")
    for j in i:
        print(j, end=",")
        print("\n")


 #Use built-in functions with tuple
print(max(nested_tuples)) 
print(min(nested_tuples))     