#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N,A,B = map(int,input().split())
    if A>B: ans = 0
    elif N==1 and A!=B: ans = 0
    else: ans = (N-2)*(B-A)+1
    
    print(ans)

if __name__ == '__main__':
    main()