#https://atcoder.jp/contests/abc143/tasks/abc143_a
A,B = map(int,input().split())
if A>=B*2:
    print(A-(B*2))
else:
    print(0)
