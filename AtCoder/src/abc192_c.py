N,K = map(str,input().split())
A = [str(i) for i in N]

for i in range(int(K)):
    g1,g2 = int(''.join(sorted(A,reverse=True))),int(''.join(sorted(A)))
    f = str(g1-g2)
    A = [j for j in f]

print(int(''.join(A)))