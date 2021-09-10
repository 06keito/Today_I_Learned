#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    array = list(map(int,input().split()))
    ans = 0
    array.sort()
    for low,high,mid in zip(range(N),range(-1,(-2)*N,-2),range(-2,(-2)*N-1,-2)):
        ans += array[mid]
    print(ans)

if __name__ == '__main__':
    main()