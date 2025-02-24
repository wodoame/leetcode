from collections import defaultdict

words = ["bdddddddddd","bbbbbbbbbbc"]
# solution 1
# def groupAnagrams(strs):
#     d = defaultdict(list)
#     for s in strs: 
#         arr = ['0'] * 26
#         for c in s:
#             index = ord(c) - ord('a')
#             arr[index] = str(int(arr[index]) + 1)
#             print(arr) 
#         key = '-'.join(arr)
#         d[key].append(s)
#     return list(d.values())

# solution 2
def groupAnagrams(strs):
    d = defaultdict(list)
    for s in strs: 
        key = ''.join(sorted(s))
        d[key].append(s)
    return list(d.values())
        
        
print(groupAnagrams(words))