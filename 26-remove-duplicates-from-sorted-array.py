def removeDuplicates(nums):
    next_index = 1
    previous = nums[0]
    for i in range(1, len(nums)):
        current = nums[i]
        nums[i] = '_'
        if current != previous: 
            nums[next_index] = current
            previous = current
            next_index += 1 
    return next_index
            
        
        
            