#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    A = set(tuple(map(int,input().split())) for _ in range(N))
    ans = 0
    #x0,x1,x2,x3,y0,y1,y2,y3
    for i in A:
        for j in A:
            x0,y0,x1,y1 = i[0],i[1],j[0],j[1]
            if x1 > x0 and y1 > y0:
                s = (x1, y0)
                t = (x0 ,y1)
                if s in A and t in A:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()