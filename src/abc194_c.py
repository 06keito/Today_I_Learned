import collections

N = int(input())
A = list(map(int,input().split()))
counter_list = collections.Counter(A)
keys = list(counter_list.keys())
ans = 0

for i in range(len(keys)-1):
    for j in range(i,len(keys)):
        value_i,value_j = keys[i],keys[j]
        count_i,count_j = counter_list[keys[i]],counter_list[keys[j]]
        ans += ((value_i-value_j)**2)*(count_i*count_j)

print(ans)