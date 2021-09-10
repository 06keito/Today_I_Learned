#https://atcoder.jp/contests/abc029/tasks/abc029_c

import itertools
N = int(input())
word = ["a","b","c"]
for i in itertools.product(word,repeat=N):
    print("".join(list(i)))
