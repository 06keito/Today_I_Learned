#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Reference https://atcoder.jp/contests/abc225/submissions/26978168

def main():
    N,M = map(int,input().split())
    B = [list(map(int,input().split())) for i in range(N)]
    flag = True

    for row_idx in range(N):
        for line_idx in range(M):
            if (line_idx+1<M) and (B[row_idx][line_idx]+1!=B[row_idx][line_idx+1]):
                flag = False
            if (row_idx+1<N) and (B[row_idx][line_idx]+7!=B[row_idx+1][line_idx]):
                flag = False
            if (line_idx!=M-1) and (B[row_idx][line_idx]%7==0): # i=1 A[idx][i%7,i+1%7,i+2%7...i+6%7]
                flag = False

    print('Yes') if flag else print('No')

if __name__ == '__main__':
    main()