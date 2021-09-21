#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    X = list(input())
    N = int(input())
    idx = []
    X_dict = {}
    for i,v in enumerate(X):
        X_dict[v] = i
    for i in range(N):
        S = list(input())
        tmp = []
        for j in S:
            tmp.append(X_dict[j])
        idx.append([tmp,''.join(S)])
    idx = sorted(idx, key=lambda x: x[0])
    for i in idx:
        print(i[1])

if __name__ == '__main__':
    main()