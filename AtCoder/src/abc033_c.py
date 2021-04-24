#https://atcoder.jp/contests/abc033/tasks/abc033_c
S = list(str(input())) +["+"]
count = 0
tmp = ""
for i in range(len(S)):
    if S[i] == "+":
        if tmp.count("0")==0:
            count += 1
        tmp = ""
    else:
        tmp += S[i]
print(count)