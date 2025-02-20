def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def sort_optimised(arr):
    for i in range(len(arr)):
        sorted=True
        for j in range(len(arr)-i-1):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                sorted=False
    if sorted:
        return arr

print(sort([2,1,5,3,8,4,6,7]))
print(sort_optimised([2,1,5,3,4,6]))