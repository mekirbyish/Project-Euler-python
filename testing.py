array = [[2,2], [5], [2,3]]
for x in range(0, len(array)):
    print(array[x]) #prints the element
    for y in array[x+1:]:
        print(y) # prints subsequent elements

