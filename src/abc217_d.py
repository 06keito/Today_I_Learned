#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reference https://kanpurin.hatenablog.com/entry/2021/09/05/163703

import bisect
import array

def main():
    L,Q = map(int,input().split())
    separator = array.array('i',[0,L])
    for _ in range(Q):
        c,x = map(int,input().split())
        y = bisect.bisect(separator,x)
        if c==1:
            separator.insert(y,x)
        else:
            print(separator[y]-separator[y-1])
            
if __name__ == '__main__':
    main()