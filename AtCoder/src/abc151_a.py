#https://atcoder.jp/contests/abc151/tasks/abc151_a

C = str(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alphabet)):
    if alphabet[i]==C:
        print(alphabet[i+1])
        break
