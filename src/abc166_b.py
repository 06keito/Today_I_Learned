#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N,K = map(int,input().split())
    array = ()
    for i in range(K):
        d = int(input())
        array += tuple(map(int,input().split()))
    print(N-len(set(array)))

if __name__ == '__main__':
    main()