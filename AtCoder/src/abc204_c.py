import sys
sys.setrecursionlimit(10000)

def dfs(array,temp,value):
    if temp[value]:
        return
    temp[value]=True #到達可能
    for i in array[value]:
        dfs(array,temp,i)


def main():
    N,M = map(int,input().split())
    # 都市iを配列で記憶し、その都市から向かうことができるリスト
    array = [[] for _ in range(N)]
    ans = 0
    for _ in range(M):
        a,b = map(int,input().split())
        array[a-1].append(b-1)
    
    for i in range(N):
        temp=[False]*N
        #都市iから都市jに到達可能か順番に見ていく
        dfs(array,temp,i)
        #print(temp)
        ans += sum(temp)
    print(ans)

if __name__ == '__main__':
    main()