N = int(input())
lst = [list(map(int,input().split())) for i in range(N)]
ans = 0

for i in range(N-1):
    for j in range(i+1,N,1):
        a = (lst[j][1]-lst[i][1])/(lst[j][0]-lst[i][0])
        if -1<=a and a<=1:
            ans += 1
print(ans)
