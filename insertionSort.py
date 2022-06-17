def insertionSort(arr): #function taking array
    for key in range (1, len(arr)): #iterate through array from index 1
        if arr[key]<arr[key-1]: #if elem < previous elem
            j = key #j takes previous index value  
            while j>0 and arr[j] < arr[j-1]: #compare indexes values
                arr[j-1],arr[j] = arr[j], arr[j-1] #swap values
                j-=1 #decrement index if swapped
    print(arr)
list1 = [6,1,8,4,10,2,77,3,453,3,7,5,2,754,8]
insertionSort(list1)    