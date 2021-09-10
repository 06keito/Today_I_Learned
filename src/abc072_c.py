#https://atcoder.jp/contests/abc072/tasks/arc082_a

import collections
N =  int(input())
a = list(map(int,input().split()))
a = collections.Counter(a)
a = sorted(a.items())
li = [0]*N
tmp = 0
if len(a)==1:
    print(a[0][1])
    exit()

for i in range(len(a)-1):
    tmp += a[i][1]
    if a[i][0]-1==a[i-1][0]:
        tmp += a[i-1][1]
    if a[i][0]+1==a[i+1][0]:
        tmp += a[i+1][1]
    li[i] = tmp
    tmp = 0

if a[-1][0]-1==a[-2][0]:
    li.append(a[-1][1]+a[-2][1])
print(max(li))
