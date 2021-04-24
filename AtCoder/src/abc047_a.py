#https://atcoder.jp/contests/abc047/tasks/abc047_a

li = list(map(int,input().split()))
li.sort(reverse=True)
if li[0] == li[1]+li[2]:
  print("Yes")
else:
  print("No")
