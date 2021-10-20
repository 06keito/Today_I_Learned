#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    array = [list(map(int,input().split())) for i in range(N)]
    ans,t = 0,0

    for a,b in array:
        t += a/b
    t /= 2

    for a,b in array:
        ans += min(a,t*b);
        t -= min(a/b,t)
    print(ans)

if __name__ == '__main__':
    main()