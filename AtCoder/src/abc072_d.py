#https://atcoder.jp/contests/abc072/tasks/arc082_b

N = int(input())
p = list(map(int,input().split()))

now = count = 0
while(now<N):
    if p[now]==now+1:
        if now+1 != N:
            tmp = p[now]
            p[now] = p[now+1]
            p[now+1] = tmp
            now -= 1
            count += 1
            continue
        else:
            tmp = p[now]
            p[now] = p[now-1]
            p[now-1] = tmp
            now -= 1
            count += 1
            continue
    now += 1
print(count)
