def divideArr(arr): #function taking an array
    if len(arr)<2: #if one element in array - base condition
        print(f"base condition reached with {arr[:]}") #print all the list(just arr[0] is printed there is one element in the list)  
    else:
        middle = len(arr)//2 # floor division - split array in 2
        print("Current list to work with: ", arr) #display array
        print("Left split: ", arr[:middle]) #show left side from 0 to middle(middle not included)
        print("Right split: ", arr[middle:]) #right side from middle to end
        l1 = divideArr(arr[:middle]) #recall the function to break down the left side
        l2 = divideArr(arr[middle:]) #recursion to break down the right side
        #implied return None
l = [8 ,6 ,2, 5, 9]
divideArr(l) #call function with the list 'l'