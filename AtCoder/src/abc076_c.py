#https://atcoder.jp/contests/abc076/tasks/abc076_c

S = str(input())
T = str(input())
N = len(S)-len(T)+1
M = len(T)
li = []

for i in range(N):
    flag = 0
    for j in range(M):
        if S[i+j]==T[j] or S[i+j] == "?":
            flag += 1
        else:
            break
    if flag == M:
        ans = S[:i]+T+S[i+M:]
        ans = ans.replace('?','a')
        li.append(ans)

if len(li)>0:
    li.sort()
    print(li[0])
else:
    print("UNRESTORABLE")
