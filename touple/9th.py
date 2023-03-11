tuple1 = (10, 20, [25, 75, 85])
# before update
print(tuple1)
# Output (10, 20, [25, 75, 85])

# modify last item's first value
tuple1[2][0] = 250
# after update
print(tuple1)
# Output (10, 20, [250, 75, 85])