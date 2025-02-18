def nextPermutation(N):
    if len(N) == 1:
        return "Not Possible"
    i = len(N) - 1
    while i > 0:
        if N[i] > N[i - 1]:
            break
        i -= 1
    if i == 0:
        return "Not Possible"
    for j in range(len(N) - 1, i - 1, -1):
        if N[i - 1] < N[j]:
            N = list(N)
            N[i - 1], N[j] = N[j], N[i - 1]
            N = ''.join(N)
            break
    N = list(N)
    N[i:] = reversed(N[i:])
    N = ''.join(N)

    return N
N = "218765"
print(nextPermutation(N))