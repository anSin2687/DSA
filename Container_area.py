#Container With Most Water

height = [1,8,6,2,5,4,8,3,7]
maxArea = 0
first = 0
last = len(height) - 1
while last > first:
    first_height = height[first]
    last_height = height[last]
    
    if first_height > last_height:
        area = last_height * (last - first)
        last -= 1
        
    else :
        area = first_height * (last - first)
        first += 1
    
    maxArea = max(maxArea,area) 