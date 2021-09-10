#https://atcoder.jp/contests/abc149/tasks/abc149_b

A,B,K = map(int,input().split())
if K>0:
    if A<=K:
        K -= A
        A = 0
        if B<=K:
            B = 0
        else:
            B -= K
    else:
        A -= K
print(A,B)
