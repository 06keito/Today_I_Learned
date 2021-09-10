#https://atcoder.jp/contests/abc047/tasks/arc063_a

S = str(input())
count = 0
now = S[0]
for i in S[1:]:
    if now!=i:
        count+=1
        now = i
print(count)
