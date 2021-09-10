#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Abstract

# run command
# -> python xxx.py

def main():
    A,B,C = map(int,input().split())
    for i in range(100):
        if A%2==1 or B%2==1 or C%2==1:
            print(i)
            exit()
        x,y,z = A,B,C
        A = (y//2)+(z//2)
        B = (x//2)+(z//2)
        C = (x//2)+(y//2)
    print(-1)

if __name__ == '__main__':
    main()