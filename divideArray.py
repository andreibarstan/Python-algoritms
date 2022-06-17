def divideArr(arr): #function taking an array
    if len(arr)<2: #if one element in array - base condition
        print(f"base condition reached with {arr[:]}") #print all the list(just arr[0] is printed there is one element in the list)  
    else:
        middle = len(arr)//2 # floor division - split array in 2
        l1 = divideArr(arr[:middle]) #recall the function to break down the left side
        l2 = divideArr(arr[middle:]) #recursion to break down the right side
        return mergeSort(l1, l2)
l = [8 ,6 ,2, 5, 9]
divideArr(l) #call function with the list 'l'