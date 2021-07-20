N = int(input())
h = list(map(int,input().split()))
lst = []
ans = 0

for i in range(max(h)):
    l,cut = 0,[]
    for r in range(1,len(h)):
        if h[r]==0 or r==len(h)-1:
            cut.append(h[l:r])
            l = r
    for j in cut:
        min_value = min(j)
        ans += min_value
        lst.append(list(map(lambda x:x-min_value,j)))
        h = 1

    print(lst,cut)