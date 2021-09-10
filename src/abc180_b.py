import math
N = int(input())
X = list(map(int,input().split()))
m,u,c = 0,0,0

for i in X:
    m += abs(i)
    u += (abs(i)**2)
    c = max(abs(i),c)
u = math.sqrt(u)
print(m)
print(u)
print(c)
