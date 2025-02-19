no_orange=int(input("Enter the number of the oranges:"))
oranges=[int(x) for x in input().split()]
k=0
for i in range(no_orange-1):
    if oranges[i]>=oranges[no_orange-1]:
        oranges[i],oranges[k]=oranges[k],oranges[i]
        k+=1
oranges[k],oranges[no_orange-1]=oranges[no_orange-1],oranges[k]
print(oranges)