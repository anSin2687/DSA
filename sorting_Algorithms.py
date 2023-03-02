nums = [10,30,1,4,46,89,32]
print(nums)

## Bubble Sorting 
def bubble_sort(array,ascending = True):
    """
    This Algorithm compares two adjacent elements 
    and then swaps them based on the order of sort.
    """
    if ascending:   # checking if the sort is to be performed in ascending or descending order
        
        for i in range(len(array)):
            # Tracking the swaps of elements
            swapped = False
            for j in range(0,len(array) - 1):
                if array[j] > array[j+1]:
                    array[j] ,array[j+1] = array[j+1],array[j] # Swapping elements if the elements are not in ascending order
                    swapped = True
            if not swapped: 
                break       # breaking the loop if there is no more swapping
    else:
        for i in range(len(array)):
            swapped = False
            for j in range(0,len(array) - 1):
                if array[j] < array[j+1]:
                    array[j] ,array[j+1] = array[j+1],array[j]
                    swapped = True
            if not swapped:
                break
    return array



def selection_sort(array,ascending = True):
    if ascending: 
        for i in range(len(array)):
            min_index = i
            for j in range(i+1,len(array)):
                if array[min_index] < array[j]:
                    min_index = j
            
            array[i],array[min_index] = array[min_index],array[i]
    else:
        for i in range(len(array)):
            min_index = i
            for j in range(i+1,len(array)):
                if array[min_index] > array[j]:
                    min_index = j
        
            array[i],array[min_index] = array[min_index],array[i]
         
    return array
    
    
def insertion_sort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            print(array[i])
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

    
def merge_sort(array):
    if len(array) > 1:
        
        mid = len(array)//2
        larr = array[:mid]
        rarr = array[mid:]
        
        merge_sort(larr)
        merge_sort(rarr)
        print("The broken arrays",larr,rarr)
        i = j = k = 0
        while i < len(larr) and j < len(rarr):
            if larr[i] < rarr[j]:
                array[k] = larr[i]
                i += 1
            else:
                array[k] = rarr[j]
                j += 1
            k += 1
        
        while i < len(larr):
            array[k] = larr[i]
            i+=1
            k+=1
        
        while j < len(rarr):
            array[k] = rarr[j]
            j+=1
            k+=1 
    
merge_sort(nums)
print(nums)


