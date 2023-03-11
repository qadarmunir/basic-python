#nested if else
num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number:"))
if num1 <= num2:
    print(num1, "is less than or equal", num2)
    if num1==num2:
     print(num1 ,"and", num2 ,"are equal")
    else:
       print(num1, "and", num2,"are not equal")
else:
     print(num1, "is geator than ", num2) 
