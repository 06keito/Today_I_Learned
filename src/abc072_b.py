#https://atcoder.jp/contests/abc072/tasks/abc072_b

s = str(input())
ans= ""
for i in range(0,len(s),1):
  if i%2 == 0:
    ans += s[i]
print(ans)
