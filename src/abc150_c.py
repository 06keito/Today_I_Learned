#https://atcoder.jp/contests/abc150/tasks/abc150_c

import itertools
import math
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
tmp = [ i for i in range(1,1+N)]
a = b = 0

for li,i in zip(itertools.permutations(tmp),range(1,math.factorial(N)+1)):
    if P==list(li):
        a = i
    if Q==list(li):
        b = i
    if a!=0 and b!=0:
        break

print(abs(a-b))
