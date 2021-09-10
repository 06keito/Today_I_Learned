#https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_a
s = str(input())
flag = 0
for i in range(len(s)):
    if s[i] == "C":
        flag += 1
        break
for j in range(i,len(s),1):
    if s[j] == "F":
        flag += 1
        break
if flag==2:
    print("Yes")
else:
    print("No")
