'''A classroom has several students, half of whom are boys and half of whom are girls. You need to arrange all of them in a line for the morning assembly
 such that the following conditions are satisfied:
The students must be in order of non-decreasing height.
Two boys or two girls must not be adjacent to each other.
You have been given the heights of the boys in the array b and the heights of the girls in the array g. Find out whether you can arrange them in an order
 which satisfies the given conditions. Print "YES" if it is possible, or "NO" if it is not.
For example, let's say there are n = 3 boys and n = 3 girls, where the boys' heights are b = [5, 3, 8] and the girls' heights are g = [2, 4, 6] . These
 students can be arranged in the order [g0, 61, 91, 60, 92, 62), which is [2. 3, 4, 5, 6, 8). Because this is in order of non-decreasing height, and no 
 two boys or two girls are adjacent to each other, this satisfies the conditions. Therefore, the answer is "YES".'''


    
def check_arrangement(arr):
    if arr[0] in b:
        for i in range(1,len(arr)):
            if i%2==0 and arr[i] not in b:
                return False
            if i%2!=0 and arr[i] not in g:
                return False
        return True
    if arr[0] in g:
        for i in range(1,len(arr)):
            if i%2==0 and arr[i] not in g:
                return False
            if i%2!=0 and arr[i] not in b:
                return False
        return True


b = [2, 5, 3]
g = [1, 4, 3]
if check_arrangement(sorted(b+g)):
    print("Yes")
else:
    print("No") 
