numbers = [1, 2, 4, 6, 8]
size=len(numbers)
for i in range(size):
    print("index is ", i, "value is", numbers[i])

name = "Jessa"
for i in name:
    print(i, end=" ") 
    print('\n') 

    #iterating string in reverse order

name = "Jessa"
for i in name[::-1]:
 print(i, end="")