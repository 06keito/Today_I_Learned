#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    p = list(map(int,input().split()))
    array = [0]*N

    for idx in range(N):
        array[p[idx]-1] = str(idx+1)
    print(' '.join(array))

if __name__ == '__main__':
    main()