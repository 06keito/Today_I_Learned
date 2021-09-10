def main():
    N = int(input())
    S_array = list(map(int,input().split()))
    T_array = list(map(int,input().split()))
    value = float('inf')
    dp = [False]*N

    for i in range(N):
        value = min(value,T_array[i])
        dp[i] = value
        value += S_array[i]

    for j in range(N):
        value = min(value,T_array[j])
        dp[j] = min(dp[j],value)
        value += S_array[j]

    for ans in dp:
        print(ans)

if __name__ == "__main__":
    main()