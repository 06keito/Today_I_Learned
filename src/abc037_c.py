#https://atcoder.jp/contests/abc037/tasks/abc037_c
N,K = map(int,input().split())
a = list(map(int,input().split()))
li = [0]*N
sum = 0

for i in range(0,N-K):
    li[i] = li[(i+1)*(-1)] = i+1

for j in range(N):
    if li[j]==0:
        sum += a[j]*(N-K+1)
    elif li[j]>K:
        sum += a[j]*K
    else:
        sum += a[j]*li[j]

print(sum)