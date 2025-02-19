def quick(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    small=[x for x in arr[:-1] if x<=pivot]
    big=[x for x in arr[:-1] if x>=pivot]
    return quick(small)+[pivot]+quick(big)