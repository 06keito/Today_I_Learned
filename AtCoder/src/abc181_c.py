N = int(input())
lst = [list(map(int,input().split())) for i in range(N)]

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            x0,y0 = lst[i]
            x1,y1 = lst[j]
            x2,y2 = lst[k]
            x0 -= x2
            x1 -= x2
            y0 -= y2
            y1 -= y2
            if x0*y1==x1*y0:
                 print("Yes")
                 exit()
print("No")