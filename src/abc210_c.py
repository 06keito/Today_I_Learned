#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reference : https://blog.hamayanhamayan.com/entry/2021/07/17/233052

from collections import Counter

def main():
    N,K = map(int,input().split())
    C = list(map(int,input().split()))
    cnt = Counter()
    kind = ans = 0
    # すべての種類のキャンディとその個数を数え上げる
    for i,c in enumerate(C):
        cnt[c] += 1
        # 新しい種類を範囲内に見つけたときの処理
        if cnt[c] == 1:
            kind += 1
        # Kの範囲を超えた場合の処理
        if i >= K:
            # 種類を記録した配列を操作する
            # i-Kの配列の場所は範囲から外れるため、数え上げから除外する
            cnt[C[i-K]] -= 1
            # もしその種類の飴がなくなってしまった場合
            if cnt[C[i-K]] == 0:
                kind -= 1
        ans = max(kind, ans)
    print(ans)

if __name__ == '__main__':
    main()