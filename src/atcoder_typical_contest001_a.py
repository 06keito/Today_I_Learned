#https://atcoder.jp/contests/atc001/tasks/dfs_a

#参考
#https://qiita.com/drken/items/a803d4fc4a727e02f7ba
#https://qiita.com/gh_takumi/items/79537ade8d2539d89bd2
#https://atcoder.jp/contests/atc001/submissions/10583695

import sys
#再帰処理の回数の上限を決める
sys.setrecursionlimit(1000000)

#再帰的な深さ優先探索
def search(h,w):
    #探索済みを示す
    reached[h][w] = 1

    #4方向への移動
    for d in range(4):
        #移動ベクトルを加算することで上下左右へ探索する
        nh = h + dx[d]
        nw = w + dy[d]

        #再帰を行うための条件
        #画面アウトせず探索する場所が未探索であること,また壁でないことないこと
        if nh>=0 and nh<H and nw>=0 and nw<W:
            if reached[nh][nw]==0 and c[nh][nw]!="#":
                search(nh,nw)
    
    #returnの必要はなく配列 reached に探索された様子がわかる

#入力の受け取り
H,W = map(int,input().split())
c = [list(str(input())) for i in range(H)]

#4方向の移動ベクトル
#[右,上,左,下]方向
dx = [1,0,-1,0]
dy = [0,1,0,-1]

#スタートとゴールのマスを特定
sw = sh = gw = gh = 0
for i in range(H):
    for j in range(W):
        if c[i][j] == "s":
            sw = j
            sh = i
        elif c[i][j] == "g":
            gw = j
            gh = i

#訪れた場所を覚えておくための配列
reached = [[0]*W for i in range(H)]

#スタートの場所から開始する
search(sh,sw)

#探索した道のりでゴールにたどり着いているかを判定する
if reached[gh][gw]==1:
    print("Yes")
else:
    print("No")
