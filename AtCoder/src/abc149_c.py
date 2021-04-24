#https://atcoder.jp/contests/abc149/tasks/abc149_c

import bisect

#エラトステネスの篩
def sieve(n):
    import math
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        #ここで篩落としてる,wikiの2番目
        data = [e for e in data if e % p != 0]



N = int(input())
A = sieve(10**5+7)

if N in A:
    print(N)
else:
    index = bisect.bisect_right(A,N)
    print(A[index])
