N = int(input())
A = list(map(int,input().split()))
ans = 0

for l in range(N):
    value = 10**7
    for r in range(l,N):
        value = min(value,A[r])
        ans = max(ans,value*(r-l+1))
print(ans)