#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Sum = sum(A)
    ans = Sum
    v = 0
    for i in range(N):
        v += A[i]
        ans  = min(ans, abs(v-(Sum-v)));
    print(ans)

if __name__ == '__main__':
    main()