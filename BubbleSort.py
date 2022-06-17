def bubble_sort(arr):
    
    swapped = True #flag to track if a swap happened
    while swapped: #if swap is true
        print("bubble sort status: " + str(arr))
        swapped = False #assume there is no swap to avoid infinite loop
        for num in range(len(arr)-1): #loop through array 
            if arr[num] > arr[num+1]: #if element > next element 
                swapped = True #when is false it means that there were no numbers swapped and the while loop breaks  
                arr[num], arr[num+1] = arr[num+1], arr[num] #swap elements
         
list1 = [5,2,3,4,1,6,8,9,10,7]
bubble_sort(list1)