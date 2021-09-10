#https://atcoder.jp/contests/abc072/tasks/abc072_a

X, t = map(int,input().split())
if t>=X:
  print("0")
else:
  print(X-t)
