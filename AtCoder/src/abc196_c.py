N = int(input())
ans = 0
for i in range(1,min(N,(10**6)),1):
    if N>=int(str(i)+str(i)):
        ans += 1
print(ans)