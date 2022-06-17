def bisectionIteration(n, arr, start, stop):
    if start > stop:
         return (f"{n} not found in list")
    else:
        middle = (start+stop)//2 #middle index 
        if n == arr[middle]: #if num is value of middle index
            return (f"{n} found at index {middle}") 
        elif n > arr[middle]: 
            return bisectionIteration(n, arr, middle+1, stop) # if num is > than value of middle index check the bigger values
        else:
            return bisectionIteration(n, arr, start, middle-1) # if num is < than value of middle index check the bigger values
    
def createList(maxVal):
    arr = []
    for num in range(1, maxVal+1):
        arr.append(num)
    return arr

l = createList(14) # create an ordered list from 1 
for num in range(16):
    print(bisectionIteration(num, l, 0, len(l)-1))