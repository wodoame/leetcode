def firstBadVersion(self, n):
    #  something similar to binary search would probably  work
    #  Although I don't remember how to implement it vividly
    # 1, 2, 3, 4, 5, 6, 7, ... 
    start = 1 
    end = n 
    c = (start + end) // 2 
    while True:
        if isBadVersion(c): 
            if not isBadVersion(c - 1): 
                return c
            end = c 
            c = (start + end) // 2 
        else:
            if isBadVersion(c + 1):
                return c + 1
            start = c
            c = (start + end) // 2


        
                     