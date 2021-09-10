r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())

if r1==r2 and c1==c2:
    print(0)
elif (r1==c1 and abs(r1-r2)<=3 and abs(c1-c2)<=3) or (r1==c1 and r2==c2):
    print(1)
elif r1==c1 or (r1!=c1 and abs(r1-r2)<=3 and abs(c1-c2)<=3):
    print(2)
else:
    print(3)
