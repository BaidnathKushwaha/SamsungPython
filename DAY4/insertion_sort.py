def sort(arr):
    for i in range(1,len(arr)):
        ele=arr[i]
        j=i-1
        while j>=0 and arr[j]>ele:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=ele
    return arr
print(sort([5,4,8,2,6,1]))