#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N,A,B = map(int,input().split())
    if (A%2==0 and B%2==0) or (A%2==1 and B%2==1):
        print((B-A)//2)
    else:
        print(min(A-1,N-B)+1+((B-A)//2))
    
if __name__ == '__main__':
    main()