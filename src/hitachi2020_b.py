#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    A,B,M = map(int,input().split())
    A_prise = list(map(int,input().split()))
    B_prise = list(map(int,input().split()))
    Most_low_prise = min(A_prise)+min(B_prise)
    for i in range(M):
        x,y,c = map(int,input().split())
        Post_coupon_orientation_prise = A_prise[x-1]+B_prise[y-1]-c
        Most_low_prise = min(Most_low_prise,Post_coupon_orientation_prise)
    print(Most_low_prise)
    
if __name__ == '__main__':
    main()