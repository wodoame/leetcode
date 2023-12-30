
def gcdOfStrings(str1, str2):
    # We need a string that divides both str1 and str2
    # By division we mean that the string we provide should be able to be used to...
    # contruct either str1 or str2 by adding to it's self multiple times (multiplication)
    # 'ababab' and 'abab' the largest common divisor is 'ab'
    # Since we want the largest common divisor we start by considering the whole string (the smaller one)
    str1_len = len(str1)
    str2_len = len(str2)
    min_len = min(str1_len, str2_len) 
    for i in range(min_len, 0, -1):
        # If the length of the word (variable i) is not divisible by either str1 or str2 (their lengths) ...
        # Then we know that it can't be added to itself any number of times to form str1 or str2
        # But if the length is divisible by both the lengths of str1 and str2 then we find by how many times...
        # (f1, f2 for factor 1 and factor 2)
        # Finally we add the string to itself using the factors to see if we get both str1 and str2
        # We check whether they are equal because the string may satisfy the divisibilty check but when it ...
        # ... is added to itself using the factors we don't get a string equal to str1 and str2
        # If we never get any match then we return an empty string
        if str1_len % i == 0 and str2_len % i == 0: 
            f1, f2 = str1_len // i, str2_len // i
            if str1[:i] * f1 == str1 and  str1[:i] * f2  == str2: 
                return str1[:i]
    return ''
            
    
        
        
        
    
    
        
print(gcdOfStrings('commoncommon', 'common'))
