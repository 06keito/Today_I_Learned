N = int(input()) 
S = list(str(input()))
Q = int(input())
even_odd_check = 0
for i in range(Q):
    T,A,B = map(int,input().split())
    A,B = A-1,B-1
    if T==1:
        if even_odd_check%2==0:
            S[A],S[B] = S[B-N],S[A-N]
        else:
            S[(A+N)%(2*N)],S[(B+N)%(2*N)] = S[(B+N)%(2*N)],S[(A+N)%(2*N)]
    else:
        even_odd_check += 1


print(S)
