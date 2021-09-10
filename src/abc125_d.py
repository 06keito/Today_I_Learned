#https://atcoder.jp/contests/abc125/tasks/abc125_d
N = int(input())
A = list(map(int,input().split()))
dp = [[0 for i in range(2)] for i in range(N+1)]
dp[0][1] = -10**9

for i in range(N):
    print(dp[i][0],dp[i][1],A[i])
    dp[i+1][0] = max(dp[i][0]+A[i],dp[i][1]-A[i])
    dp[i+1][1] = max(dp[i][0]-A[i],dp[i][1]+A[i])

print(dp[N][0])