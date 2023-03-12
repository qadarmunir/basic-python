odd = [1, 5, 7, 9]
even= [i+1 for i in odd if i%2==1]
print(even)

#Accessing the index in for loop
numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]
for i,v in enumerate(numbers):
    print(i,v)