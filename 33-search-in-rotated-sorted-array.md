```python
def search(nums, target):
    i = 0
    previous = nums[0]
    while i < len(nums):
        if nums[i] == target: 
            return i 
        
        if nums[i] < previous:
            break
        
        previous = nums[i]
        i += 1 
        
    start = i + 1
    end = len(nums) - 1 
    
    while start <= end:
        mid = (start + end) // 2 
        mid_element = nums[mid]
        if mid_element  == target:
            return mid
        elif mid_element < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1
        
nums = [4, 5, 6, 7, 0, 1, 2, 3]

# I checked the left sorted part linearly and the right part logarithmically but that's not good enough even though my solution was accepted
# I must check both sides logarithmically

```
```python
# So I looked at solutions that run faster and I found a new way to solve it

def search(nums, target):
    return bin_search(nums, target, 0, len(nums) - 1)
  
def bin_search(nums, target, start, end):
    if start > end: 
        return -1
    
    mid = (start + end) // 2
    mid_element = nums[mid]
    
    if mid_element == target: # condition a
        return mid
    elif nums[start] <= target < mid_element: # condition b
        return bin_search(nums, target, start, mid - 1)
    elif mid_element < target <= nums[end]: # condition c
        return bin_search(nums, target, mid + 1, end)
    elif mid_element < nums[start]: # then condition b must have failed because of mid_element is less than nums[start], this also means that target is not present at condition c
        return bin_search(nums, target, start, mid - 1)
    else: # condition b must have failed because target is not present
        return bin_search(nums, target, mid + 1, end)
        
```

```python
# Another solution I saw

def search(self, nums, target):
    l, r = 0, len(nums) -1
    while l <= r:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:

                l = mid+1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

```

            
            
        
        
        