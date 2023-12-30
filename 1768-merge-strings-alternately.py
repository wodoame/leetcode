def mergeAlternately(word1, word2):
    result = ''
    min_len = min(len(word1), len(word2))
    for i in range(min_len):
        result += word1[i] + word2[i]
        
    if len(word1) > len(word2): 
        return result + word1[min_len:]
    elif len(word1) < len(word2): 
        return result + word2[min_len:]
    return result

word1 = 'abcd'
word2 = 'pq'

print(mergeAlternately(word1, word2))