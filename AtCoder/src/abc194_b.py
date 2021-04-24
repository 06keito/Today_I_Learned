N = int(input())
li = [list(map(int,input().split())) for i in range(N)]
ans = 10**9

for idx_a in range(N):
    for idx_b in range(N):
        A,B = li[idx_a][0],li[idx_b][1]
        if idx_a==idx_b:
            ans = min(ans,A+B)
        else:
            ans = min(ans,max(A,B))
print(ans)