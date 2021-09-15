#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    Q,H,S,D = map(int,input().split())
    N = int(input())
    best_half = min(Q*2,H)
    best_scale = min(best_half*2,S)
    best_dual = min(best_scale*2,D)
    cost = 0
    if N>1:
        cost += best_dual*(N//2)
        N %= 2
    if N==1:
        cost += best_scale
        N -= 1
    print(cost)

if __name__ == '__main__':
    main()