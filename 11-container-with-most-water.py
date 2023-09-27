def maxArea(height):
    start = 0
    end = len(height) - 1
    max_area = 0
    largest_height = max(height)
    while start < end: 
        a = height[start - 1]
        b = height[end - 1]
        area = (end - start) * min(a, b)
        max_area = max(area, max_area)
        if a < b: 
            start += 1
        else: 
            end -= 1
        
        # further optimization
        if max_area >= largest_height * (end - start): 
            break  # i.e we should stop since we won't obtain a bigger area than the current maximum area we have
                   # If the largest height multiplied by the remaining length won't exceed our current maximum then smaller heights certainly wouldn't    
    return max_area
        
        
        
        
    
