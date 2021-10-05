#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def main():
    N = int(input())
    A = list(map(int,input().split()))
    X = int(input())
    value = (X//sum(A))*sum(A)
    ans = (X//sum(A))*N
    for i in A:
        value += i
        ans += 1
        if value>X:
            print(ans)
            break

if __name__ == '__main__':
    main()