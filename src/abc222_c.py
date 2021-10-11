#!/usr/bin/env python
# -*- coding: utf-8 -*-

def result(hand1,hand2):
    if (hand1=='G' and hand2=='C')or(hand1=='C' and hand2=='P')or(hand1=='P' and hand2=='G'):
        return 'p1win'
    elif (hand1=='C' and hand2=='G')or(hand1=='P' and hand2=='C')or(hand1=='G' and hand2=='P'):
        return 'p2win'
    else:
        return 'draw'

def main():
    N,M = map(int,input().split())
    A = [list(map(str,input())) for _ in range(2*N)]
    rank = [[i,0] for i in range(2*N)]

    for i in range(M):
        hand = []
        for j in range(2*N):
            hand.append(A[j][i])
        for k in range(0,2*N,2):
            R = result(hand[rank[k][0]],hand[rank[k+1][0]])
            if R=='p1win':
                rank[k][1] -= 1
            elif R=='p2win':
                rank[k+1][1] -= 1
            else:
                continue
        rank = sorted(rank, key=lambda x:(x[1],x[0]))
    
    for r,w in rank:
        print(r+1)

if __name__ == '__main__':
    main()