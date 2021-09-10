#https://atcoder.jp/contests/abc151/tasks/abc151_c

N,M = map(int,input().split())
WAlist = [[0,"WA"]  for i in range(N)]
AC = WA = 0
for i in range(M):
    p,S = input().split()
    p = int(p)
    if S=="WA"and WAlist[p-1][1]=="WA":
        WAlist[p-1][0] += 1
    elif S=="WA" and WAlist[p-1][1]=="AC" or S=="AC"and WAlist[p-1][1]=="AC":
        continue
    elif S=="AC" and WAlist[p-1][1]=="WA":
        WAlist[p-1][1] = "AC"
        AC += 1

for j in range(N):
    if WAlist[j][1]=="AC":
        WA += WAlist[j][0]

print(AC,WA)
