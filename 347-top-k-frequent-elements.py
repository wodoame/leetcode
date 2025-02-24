from collections import defaultdict
import heapq 

nums = [0, 0, 0, 0, 0, 0, 0, 1,1,1,2,2,3, 3, 3, 3, 3, 3, 3,3, 3, 3, 3, 3, 3, 3]
# def topKFrequent(nums: list, k):
#     d = defaultdict(int)
#     ans = []
#     for num in nums:
#         d[num] += 1
    
#     x = sorted(d.values(), reverse=True)[:k]
#     for key, value in d.items():
#         if value in x:
#             ans.append(key)
#     return ans

# solution 2
# def topKFrequent(nums: list, k):
#     d = defaultdict(int)
#     for num in nums:
#         d[num] += 1
    
#     heap = [(value, key) for key, value in d.items()]
#     heapq.heapify(heap)
#     return [val[1] for val in heapq.nlargest(k, heap)]

def topKFrequent(nums, k):
    # Step 1: Count the frequency of each number
    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1
    
    # Step 2: Create a list of buckets where the index represents frequency
    # The maximum possible frequency is len(nums)
    max_freq = max(freq_map.values())
    buckets = [[] for _ in range(max_freq + 1)]
    
    # Step 3: Group numbers by their frequency
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    # Step 4: Extract the top k frequent numbers
    ans = []
    for i in range(max_freq, 0, -1):  # Iterate from highest frequency to lowest
        if buckets[i]:  # If there are numbers with this frequency
            ans.extend(buckets[i])  # Add them to the answer
            if len(ans) >= k:  # Stop once we have k numbers
                break 
    
    # Return only the first k elements (in case we added more than k)
    return ans[:k]

print(topKFrequent(nums, 3)) # [1, 2]
    
    
    