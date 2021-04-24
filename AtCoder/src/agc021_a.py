#https://atcoder.jp/contests/agc021/tasks/agc021_a
N = str(input())
K = len(N)
c = int(N[0])
for i in N[1:]:
    if i!="9":
        #もし最初の桁以外に9が出現したとき
        print(c+9*(K-1)-1)
        break
        #exit()
print(c+9*(K-1))
