#Pass Statement in for loop
number=[1,2,3,4,5,6,7,8,9,10]
for i in number:
    pass

#else block in for loop
for i in range(1,10):
    if i<=10:
        print(i)
    else:
        print("done")    

#bothelse and break statement in for loop
count=0
for i in range(1,10):
    count=count+1
    if i<2:
        
        break
    else:
        print(i)
else:
    print("done")