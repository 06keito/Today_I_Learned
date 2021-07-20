A,B,C = map(int,input().split())
powA,powB = A**2,B**2
if C%2==0:
    if powA==powB:
        print("=")
    elif powA>powB:
        print(">")
    elif powA<powB:
        print("<")
elif C%2==1:
    if A==B:
        print("=")
    elif A>B and A>=0:
        print(">")
    elif A<B and B>=0:
        print("<")
