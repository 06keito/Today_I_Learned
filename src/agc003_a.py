#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check(S,a,b):
    if (a in S) and (b not in S): 
        return 0
    if (b in S) and (a not in S):
        return 0
    return 1

def main():
    S = str(input())
    flag = 1
    for a,b in [['N','S'],['E','W']]:
        flag = min(check(S,a,b),flag)
    if flag==1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()