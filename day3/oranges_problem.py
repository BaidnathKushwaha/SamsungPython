#The first line of input is n (1sn≤100), the number of oranges Tisha plucked from the orchard The second line of input are the diameters of the oranges 
# you just took (positive numbers) each separated by a space. Assume the last orange (orange[n-1]) to be the one Tisha took in her hand.

no_orange=int(input("Enter the number of the oranges:"))
oranges=[int(x) for x in input().split()]
k=0
for i in range(no_orange-1):
    if oranges[i]<=oranges[no_orange-1]:
        oranges[i],oranges[k]=oranges[k],oranges[i]
        k+=1
oranges[k],oranges[no_orange-1]=oranges[no_orange-1],oranges[k]
print(oranges)