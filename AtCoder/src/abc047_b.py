#https://atcoder.jp/contests/abc047/tasks/abc047_b

W,H,N = map(int,input().split())
bo = [[0]*W]*H
for i in range(N):
    x,y,z = map(int,input().split())
    if z == 1:
        for j in range(H):
            for k in range(x):
                bo[j][k] = 1
    elif z == 2:
        for j in range(H):
            for k in range(x,W,1):
                bo[j][k] = 1
    elif z == 3:
        for j in range(y):
            bo[j] = [1]*W
    else:
        for j in range(H-1,y-1,-1):
            bo[j] = [1]*W

sum = 0

for i in range(H-1,-1,-1):
    sum += bo[i][:].count(1)
print((W*H)-sum)
