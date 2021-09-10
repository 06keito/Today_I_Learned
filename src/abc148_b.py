#https://atcoder.jp/contests/abc148/tasks/abc148_b

N = int(input())
S,T = map(str,input().split())
ans = ""
for i in range(N*2):
    if i%2==0:
        ans += S[i//2]
    else:
        ans += T[i//2]
print(ans)

