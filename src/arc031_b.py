#https://atcoder.jp/contests/arc031/tasks/arc031_2

import sys
sys.setrecursionlimit(1000000)

def search(h,w):
    reached[h][w] = "o"
    
    for d in range(4):
        nh = h + dx[d]
        nw = w + dy[d]
        if nh>=0 and nh<H and nw>=0 and nw<W:
            if reached[nh][nw]=="x" and A[nh][nw]!="x":
                search(nh,nw)

A = [ list(str(input())) for i in range(10) ]
H = len(A)
W = len(A[0])

#4方向の移動ベクトル
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for h in range(10):
    for w in range(10):
        reached = [["x"]*10 for i in range(10)]
        #元が埋め立てられてるかどうか
        if A[h][w] == "o":
            flag = 0 #のちの処理は行わない
        else:
            flag = 1
            A[h][w] = "o" #元の形に戻す必要がある
        search(h,w)
        if reached == A:
            print("YES")
            exit()
        else:
            if flag == 1:
                A[h][w] = "x"

print("NO")