N = int(input())
S = len(str(N))
ans = 0

for i in range(3,S,3):
    value = 10**i
    ans += (N-int(value))+1

print(ans)
