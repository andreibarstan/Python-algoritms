def mergeSort(arr1, arr2): #function takes 2 arrays
    sortedArr = [] #initialise as empty array
    i, j= 0, 0 #both array indexes set to 0
    while i < len(arr1) and j<len(arr2): #loop through both arrays, compare elem of each index and add the smallest to the sortedArray
        if arr1[i]< arr2[j]:
            sortedArr.append(arr1[i])
            i+=1
        else:
            sortedArr.append(arr2[j])
            j+=1
    while len(arr1)>i or len(arr2) > j:  #when one index reaches the end, but there are still elements left in the other array, append remaining elem to sortedArray
        if i<len(arr1):
            sortedArr.append(arr1[i])
            i+=1
        elif j<len(arr2):
            sortedArr.append(arr2[j])
            j+=1
    return sortedArr

def divideArr(arr): #function taking an array
    if len(arr)<2: #if one element in array - base condition
        return arr[:] #returns all the list(just arr[0] is printed there is one element in the list)
    else:
        middle = len(arr)//2 # floor division - split array in 2
        l1 = divideArr(arr[:middle]) #recall the function to break down the left side
        l2 = divideArr(arr[middle:]) #recursion to break down the right side
        return mergeSort(l1, l2)
        
l = [8 ,6 ,2, 5, 9, 22, 0]
print(divideArr(l)) #call function with the list 'l'
# l1 = [2, 3, 5, 7 ,8 ,9,11,13]
# l2 = [1, 4, 6, 8, 10, 11, 12]
# print (f"Unmerged list: {mergeSort(l1, l2)}")