N,X = map(int,input().split())
limit,count = 0,0
for i in range(N):
    V,P = map(int,input().split())
    limit += V*P
    count += 1
    if X*100<limit:
        print(count)
        exit()
print(-1)