import itertools
import collections

N,M = map(int,input().split())
flag = [list(map(int,input().split())) for _ in range(M)]
flag = tuple(map(lambda x: tuple(list(sorted(x))), flag))
flag = collections.Counter(flag)
K = int(input())
choice = [list(map(int,input().split())) for _ in range(K)]
ans = 0

for i in range(2**K):
    value = 0
    select = []
    for j in range(K):
        if ((i >> j) & 1):
            select.append(choice[j][0])
        else:
            select.append(choice[j][1])
    select = list(set(select))
    combo = list(itertools.combinations(select, 2))
    combo = tuple(set(map(lambda x: tuple(list(sorted(x))), combo)))
    for t in combo:
        value += flag[t]
    ans = max(ans,value)
print(ans)
