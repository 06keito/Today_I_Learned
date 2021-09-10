#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    k = 0

    while(True):
        if 2**k>N:
            print(k-1)
            break
        k += 1

if __name__ == '__main__':
    main()