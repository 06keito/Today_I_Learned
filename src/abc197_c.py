#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Reference https://ebisuke33.hatenablog.com/entry/abc197c

def main():
    N = int(input())
    array = list(map(int,input().split()))
    ans = 10**9+7
    if N==1:
        print(array[0])
        exit()
    for i in range(2**(N-1)):
        base = 0
        or_value = array[0]
        for j in range(1,N):
            if (i>>(j-1)) & 1:
                base ^= or_value
                or_value = 0
                or_value |= array[j]
            else:
                or_value |= array[j]
        base ^= or_value
        ans = min(ans,base)
    print(ans)

if __name__ == '__main__':
    main()