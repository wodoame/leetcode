def lengthOfLongestSubstring(self, s): 
    i, j = 0, 0
    max_length = 0
    charset = set()
    string_length = len(s)
    while i < string_length: 
        letter = s[i]
        if letter not in charset: 
            charset.add(letter)
            i += 1
            max_length = max(max_length, i - j)
        else: 
            charset.remove(s[j])
            j += 1 
    return max_length
        

        
        