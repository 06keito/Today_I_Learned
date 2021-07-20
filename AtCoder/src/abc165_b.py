from decimal import Decimal

X = Decimal(str(input()))
N = Decimal(100)
count = 0

while(X>N):
    count += 1
    N = Decimal(int(N*(Decimal(101)/Decimal(100))))

print(count)