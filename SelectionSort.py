def selection_sort(arr): #function takink the array 'arr'
    indexPosition = 0 #starting from index 0
    while indexPosition < len(arr): #outer loop going 
        for num in range(indexPosition, len(arr)): #loop iterating through each index
            if arr[indexPosition] > arr[num]: #value of each index is compared to value of num
                arr[indexPosition], arr[num]= arr[num], arr[indexPosition]# swap array elements        
        print(arr)
        indexPosition+=1 #increm index and form the ordered array

list1 = [6,8,1,4,7,8,9,3,2,5,10]
selection_sort(list1)