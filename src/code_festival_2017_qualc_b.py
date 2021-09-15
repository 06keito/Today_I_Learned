#!/usr/bin/env python
# -*- coding: utf-8 -*-

def different_solution(array):
    even = 0
    for i in array:
        if i%2==0:
            even += 1
    ans = 3**len(array)-(2**even)
    return ans

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(3**N):
        tmp = 1
        S = base10int(i,3).zfill(N)
        for j in range(N):
            tmp  *= A[j]+int(S[j])-1
        if tmp%2==0:
            ans += 1 
    print(ans)

if __name__ == '__main__':
    main()