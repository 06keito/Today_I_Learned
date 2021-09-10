import collections

N = int(input())
A = list(map(int,input().split()))
lst = collections.Counter(A)
ans = (N*(N-1))//2

for key,value in lst.items():
    if value>1:
        ans -= (value*(value-1))//2
print(ans)