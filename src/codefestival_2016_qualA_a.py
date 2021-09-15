#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    array = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if array[array[i]-1]==i+1:
            ans += 1
    print(ans//2)

if __name__ == '__main__':
    main()