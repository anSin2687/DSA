nums = [10,30,1,4,46,89]
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




bubble_sort(nums,ascending=False)
print(nums)


