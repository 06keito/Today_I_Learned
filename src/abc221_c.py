#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    S = str(input())
    N = [int(i) for i in S] 
    ans = 0
    for i in range(1,2**len(N)-1):
        a,b = [],[]
        for j in range(len(N)):
            if ((i >> j) & 1):
                a.append(N[j])
            else:
                b.append(N[j])
        a.sort(reverse=True)
        b.sort(reverse=True)
        A = int("".join(map(str, a)))
        B = int("".join(map(str, b)))
        ans = max(ans,A*B)
    print(ans)

if __name__ == '__main__':
    main()