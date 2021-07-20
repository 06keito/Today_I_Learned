from scipy.special import comb
import itertools

def func(S):
    A,B = [],[]
    for n,c in enumerate(S):
        if c=="o":
            A.append(n)
        elif c=="?":
            B.append(n)
    if len(A)>4:
        print(0)
        exit()
    return A,B

S = str(input())
A,B = func(S)
ans = len(A)**4
print(A,B,ans)

for i in raneg()