#https://atcoder.jp/contests/abc149/tasks/abc149_d

N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = str(input())

BAN = [""]*N
score = 0

for i in range(K):#手が制限されるまではどんな手を出そうが問題はない
    if T[i]=="r":
        score += P
        BAN[i] = "p"
    elif T[i]=="s":
        score += R
        BAN[i] = "r"
    else:
        score += S
        BAN[i] = "s"


for j in range(K,N):
    if T[j]=="r":#相手の手はなんですか
        if BAN[j-K]=="p" :#もしこの手がBANされたものであるならあいこまたは負けの処理
            continue
        else:#でなければ得点になりK回先の手が制限される
            score += P
            BAN[j] = "p"
    elif T[j] == "s":
        if BAN[j-K] == "r":
            continue
        else:
            score += R
            BAN[j] = "r"
    else:
        if BAN[j-K] == "s":
            continue
        else:
            score += S
            BAN[j] = "s"

print(score)
