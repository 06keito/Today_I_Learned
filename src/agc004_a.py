#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    A,B,C = map(int,input().split())
    if A%2==1 and B%2==1 and C%2==1:
        print(min(A*B,A*C,B*C))
    else:
        print(0)

    
if __name__ == '__main__':
    main()