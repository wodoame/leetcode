def minimumAbsDifference(arr):
    arr.sort()
    result = []
    minimum = abs(arr[0] - arr[1])
    for i in range(len(arr) - 1): 
        a = arr[i]
        b = arr[i + 1]
        difference = abs(a - b)
        if difference == minimum:
            result.append([a, b])
        elif difference < minimum: 
            minimum = difference
            result.clear()
            result.append([a, b])
    return result
