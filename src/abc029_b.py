#https://atcoder.jp/contests/abc029/tasks/abc029_b

count = 0
S = [str(input()) for i in range(12)]
for i in range(12):
    for j in range(len(S[i])):
        if S[i][j] == "r":
            count += 1
            break
print(count)
