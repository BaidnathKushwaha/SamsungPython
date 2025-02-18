def search(arr,target):
    s=0
    e=len(arr)-1
    while (s<=e):
        mid=s+(e-s)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<=target:
            s=mid+1
        else:
            e=mid-1
    return -1
ar=[2,4,6,8,10]
tar=int(input("Enter the number to find:"))
pos=search(ar,tar)
if pos==-1:
    print("not found")
else:
    print("found at position:",pos+1)