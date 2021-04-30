def flag(a,b,c):
    if a+b>c and b+c>a and c+a>b and a!=b and b!=c and a!=c:
        return True
    return False

N = int(input())
L = list(map(int,input().split()))
count = 0

for i in range(0,N-2,1):
    for j in range(i+1,N-1,1):
        for k in range(j+1,N,1):
            if flag(L[i],L[j],L[k])==True:
                count += 1
print(count)