def productExceptSelf(nums):
    l = len(nums)
    output = [0] * l # create an array the same size as nums
    pre = 1
    for i in range(l):
        output[i] = pre # store the current prefix in output at the same position as num[i] i.e output[i]
        pre *= nums[i] # compute the prefix for the next number
    
    post = 1
    for i in range(l - 1, -1, -1):
        output[i] *= post # multiply the postfix by the prefix that's already available for the current number
        post *= nums[i] # compute the postfix for the next number
    return output