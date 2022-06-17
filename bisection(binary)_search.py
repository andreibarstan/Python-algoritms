def bisectionIteration(n, arr):
    start = 0 #start index
    stop = len(arr)-1 #end index
    while start <= stop: #while value is in the list
        middle = (start+stop)//2 #middle index 
        if n == arr[middle]: #if num is value of middle index
            return (f"{n} found at index {middle}") 
        elif n > arr[middle]: 
            start = middle + 1 # if num is > than value of middle index check the bigger values
        else:
            stop = middle - 1 # check smaller values than 
    return (f"{n} not found in list")
    

def createList(maxVal):
    arr = []
    for num in range(1, maxVal+1):
        arr.append(num)
    return arr

l = createList(14)
for num in range(16):
    print(bisectionIteration(num, l))