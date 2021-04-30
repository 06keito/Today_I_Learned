X = int(input())
N = 100
count = 0

while(X>N):
    count += 1
    N = int(N*(101/100))

print(count)