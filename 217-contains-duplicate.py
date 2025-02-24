nums = [1, 2, 3]
seenNumbers = set() 
def containsDuplicate(nums):
    for num in nums: 
        if num in seenNumbers:
            return True
        seenNumbers.add(num)
    return False 

print(containsDuplicate(nums))
        