    
def numTrees(t: int) -> int:
    a = [0 for i in range(t + 1)]
    a[0] = 1 #for beauty
    for n in range(1, t + 1):
        for i in range(n):
            j = n - 1 - i
            a[n] += a[i]*a[j]
    return a[t]

print(numTrees(2))