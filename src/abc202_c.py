import collections

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

Z = collections.Counter([B[i-1] for i in C])
A = collections.Counter(A)

ans = 0

for key_a,value_a in A.items():
    ans += Z[key_a]*value_a

print(ans)