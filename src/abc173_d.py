#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reference https://blog.hamayanhamayan.com/entry/2020/07/05/235409

from math import ceil

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N-1):
        ans += A[ceil(i/2)]
    print(ans)
    
if __name__ == '__main__':
    main()