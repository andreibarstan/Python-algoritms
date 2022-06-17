def quickSort(arr):
    """
    Input: Unsorted list of integers
    Returns sorted list of integers using quick sort
    """
    if len(arr)<2: #base case when down to one item 
        return arr
    else: 
        pivot = arr[-1] # pivot is a random element from array (the last one in this case) that is used to compare to other elements
        smaller, equal, larger = [],[],[] #lists storing elements related to pivot. EX: if an elem is smaller than pivot it goes in 'smaller' list
        for num in arr: # iterate through arr
            if num < pivot: 
                smaller.append(num) #add num to list
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quickSort(smaller) + equal + quickSort(larger) #  takes each list and sorts it recursively 

l = [6,8,1,4,10,7,8,9,3,2,5]
print(quickSort(l))