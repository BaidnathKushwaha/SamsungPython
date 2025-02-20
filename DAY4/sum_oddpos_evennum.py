def sum_string(num):
    num=str(num)
    s=0
    for i in num[::2]:
        i=int(i)
        if(i%2==0):
            s=s+i
    return s

def sum_num(num):
    s=0
    if len(str(num))%2==0:
        num=num//10
    while(num>0):
        if (num%10)%2==0:
            s+=num%10
        num=num//100
    return s
print(sum_string(12346))
print(sum_num(1244))
print(sum_num(12446))