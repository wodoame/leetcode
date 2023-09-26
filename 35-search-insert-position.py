def searchInsert(arr, target): 
    start = 0
    end = len(arr) - 1
    while start <= end:         
        mid = (start + end) // 2  # i.e mid - start = end - mid ; 2mid =  start + end 
        mid_element = arr[mid]
        if target == mid_element: 
            return mid
        elif mid_element < target: 
            start = mid + 1
        else: 
            end = mid - 1
    return start
            