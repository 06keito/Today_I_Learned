#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    array = [list(map(int,input().split())) for i in range(N)]
    ans = 0
    for i in range(N-2):
        x1,y1 = array[i][0],array[i][1]
        for j in range(i+1,N-1):
            x2,y2 = array[j][0],array[j][1]
            for k in range(j+1,N):
                x3,y3 = array[k][0],array[k][1]
                v = abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2
                if v>0:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()