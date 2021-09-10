import collections
from scipy.special import comb

def nCr(n,r):
    return comb(n, r, exact=True)

N = int(input())
A = list(map(int,input().split()))
A = list(map(lambda x:x%200,A))
C = collections.Counter(A)
ans = 0

for key,value in C.items():
    if value>1:
        ans += nCr(value,2)

print(ans)

