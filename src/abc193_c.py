N = int(input())
lst = []
max_a = int(N**0.5)
for a in range(2,min(N,10**5),1):
    for b in range(2,100,1):
        if a**b<=N:
            lst.append(a**b)
        else:
            break

print(N - len(list(set(lst))))