import math
inputed_num=int(input("Enter a number"))
root_num=math.sqrt(inputed_num)
print(root_num)
if(root_num**2==inputed_num):
    print("perfect number")
else:
    print("not a perfect number")