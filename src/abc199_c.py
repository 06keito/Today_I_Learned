#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reference : (https://blog.hamayanhamayan.com/entry/2021/04/25/002202)

def main():
    N = int(input())
    S = list(input())
    pre,post = S[:N],S[N:]
    Q = int(input())

    for i in range(Q):
        T,A,B = map(int,input().split())
        A,B = A-1,B-1 #index処理対策
        if T==1: #A<Bが条件となっている
            if B<N: #前半部だけのswap処理
                pre[A],pre[B] = pre[B],pre[A]
            elif N<=A: #後半部のswap処理
                post[A-N],post[B-N] = post[B-N],post[A-N]
            else: #A<=N<Bの処理
                pre[A],post[B-N] = post[B-N],pre[A]
        else: #T==2は前半部と後半部をswapさせるだけで良い
            pre,post = post,pre
    print(''.join(pre+post))

if __name__ == '__main__':
    main()