#https://atcoder.jp/contests/abc028/tasks/abc028_c
li = list(map(int,input().split()))
ans = []
for i in range(0,4):
    for j in range(i+1,4):
        for k in range(j+1,5):
            #print(i,j,k)
            ans.append(li[i]+li[j]+li[k])


ans = list(set(ans))
ans.sort()
print(ans[-3])
