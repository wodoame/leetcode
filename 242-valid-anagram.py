# solution 1
# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
#     return sorted(s) == sorted(t)

# solution 2
from collections import defaultdict
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    d = defaultdict(int)
    for i in range(len(s)):
        d[s[i]] += 1 # increment the count of a character. eg {'a': 1}
        d[t[i]] -= 1 # decrement the count of a character. eg {'a': 0}
    
    for value in d.values():
        if value != 0:
            return False
    return True        

# solution 3        

# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
#     d = [0] * 26
#     for i in range(len(s)):
#         a = ord(s[i]) - ord('a') 
#         b = ord(t[i]) - ord('a') 
#         d[a] += 1
#         d[b] -= 1
#     for value in d:
#         if value != 0:
#             return False
#     return True        

print(isAnagram('aacc', 'ccaa')) # True
