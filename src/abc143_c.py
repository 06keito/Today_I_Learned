#https://atcoder.jp/contests/abc143/tasks/abc143_c
N = int(input())
S = str(input())
tmp = S[0]
ans = ""
for i in range(1,N):
    if tmp != S[i]:
        ans += tmp
        tmp = S[i]
ans += tmp
print(len(ans))
