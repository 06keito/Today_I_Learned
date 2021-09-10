#https://atcoder.jp/contests/abc151/tasks/abc151_b

N,K,M = map(int,input().split())
A = list(map(int,input().split()))
score = sum(A)

for i in range(K+1):
    if (score+i)/N>=M:
        print(i)
        exit()
print("-1")
