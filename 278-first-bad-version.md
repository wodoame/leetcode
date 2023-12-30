```python
def firstBadVersion(self, n):
    # The concept of binary search was used 
    # 1, 2, 3, 4, 5, 6, 7, ... 
    # isBadVersion() is provided by leetcode
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
```


        
                     