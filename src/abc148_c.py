#https://atcoder.jp/contests/abc148/tasks/abc148_c

def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

A,B = map(int,input().split())
print((A*B)//gcd(A,B))