#https://abc007.contest.atcoder.jp/tasks/abc007_3

#参考
#https://qiita.com/drken/items/996d80bcae64649a6580
#https://udomomo.hatenablog.com/entry/2018/04/16/215915
#https://ja.wikipedia.org/wiki/%E5%B9%85%E5%84%AA%E5%85%88%E6%8E%A2%E7%B4%A2

from collections import deque
import sys
sys.setrecursionlimit(1000000)
def bfs(c,visited,sh,sw,gh,gw):
    queue = deque([[sh,sw]])
    visited[sh][sw] = 0 #訪れたことを示す 0を代入する

    while queue:
        y,x = queue.popleft() #queueから取り出しを行う
        if [y,x] == [gh,gw]: #ゴールに到達した際の処理
            return visited[y][x]
        for d in range(4):
            nh = y + dx[d] #上下左右への移動をするための変数
            nw = x + dy[d]
            if c[nh][nw]== "." and visited[nh][nw]== -1 : #移動先が通行可能であること、および移動先が未探索であること
                visited[nh][nw] = visited[y][x] + 1
                queue.append([nh,nw])


H,W = map(int,input().split()) #行と列の総数

sh,sw = map(int,input().split()) #スタート、ゴールの位置の取得
gh,gw = map(int,input().split())

sh,sw,gh,gw = sh-1,sw-1,gh-1,gw-1

c = [ list(str(input())) for i in range(H) ] #使用するグリッド

visited = [[-1]*W for i in range(H)] #訪れた場所を記録する、-1で初期化

#4方向の移動ベクトル
#[右,上,左,下]方向に対応
dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = bfs(c,visited,sh,sw,gh,gw)

print(ans)
