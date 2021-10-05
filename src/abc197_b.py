#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check(N,S):
    if S=='.':
        return N+1,False
    else:
        return N,True

def main():
    H,W,X,Y = map(int,input().split())
    S = [list(map(str,input())) for i in range(H)]
    X -= 1
    Y -= 1
    ans = -3

    for i in range(X,H,1):
        ans,flag = check(ans,S[i][Y])
        if flag: break
    for i in range(X,-1,-1):
        ans,flag = check(ans,S[i][Y])
        if flag: break
    for j in range(Y,W,1):
        ans,flag = check(ans,S[X][j])
        if flag: break
    for j in range(Y,-1,-1):
        ans,flag = check(ans,S[X][j])
        if flag: break
    print(ans)

if __name__ == '__main__':
    main()