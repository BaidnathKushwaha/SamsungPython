def sort(st):
    arr=list(st)
    for i in range(1,len(arr)):
        ele=arr[i]
        j=i-1
        while j>=0 and arr[j]>ele:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=ele
    return "".join(arr)
def word_split(line):
    word=line.split()
    for i in range(len(word)):
        word[i]=sort(word[i])
    return " ".join(word)

print(word_split('abc abcc acb atr'))