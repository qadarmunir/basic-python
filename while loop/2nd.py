number=int(input("enter a number between 100 and 500:"))
while number<100 or number>500:
    print("number is out of range")
    number=int(input("enter a number between 100 and 500:"))
else:
    print("number is in range")    