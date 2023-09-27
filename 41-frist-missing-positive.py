def firstMissingPositive(self, arr: List[int]) -> int:
    arr.sort()
    minimum = 1
    previous = 0
    for element in arr: 
        if element <= 0 or element == previous: 
            continue
        if element > minimum:
            return minimum
        else: 
            minimum += 1
            previous = element
    return minimum