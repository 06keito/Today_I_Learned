#https://atcoder.jp/contests/abc148/tasks/abc148_d

N = int(input())
A = list(map(int,input().split()))
ans = 0
now = 1
for i in A:
    if now==i:
        now += 1
    else:
        ans += 1
if ans == N:
    print(-1)
else:
    print(ans)
