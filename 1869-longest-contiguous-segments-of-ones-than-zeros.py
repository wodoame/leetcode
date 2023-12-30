
def checkZeroOnes(s): 
    max_1  = 0 
    max_0 = 0
    one_count = 0
    zero_count = 0
    for digit in s:
        if digit == '1': 
            # If we encounter a 1 then it means we have finished counting contiguous 0's. 
            # We need to reset the zero's count too
            one_count += 1 
            zero_count = 0
        else: 
            zero_count += 1
            one_count = 0
        
        # We update the max_1 and max_0 after every iteration. 
        max_1 = max(max_1, one_count)
        max_0 = max(max_0, zero_count)


    print(max_1, max_0)
    return max_1 > max_0

s = "11100011111"


print(checkZeroOnes(s))
        
