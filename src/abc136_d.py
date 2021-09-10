#https://atcoder.jp/contests/abc136/tasks/abc136_d

S = str(input())+"R"

li = [0]*len(S)
count,index = 0,0

for i in range(len(S)-1):
    if S[i]!=S[i+1] and S[i+1] == "L":
        index = i
    count += 1

    if S[i]!=S[i+1] and S[i+1] == "R":
        count_R = i-index
        count_L = count-count_R
        li[index] = (count_R//2)+(count_L//2+count_L%2)
        li[index+1] = (count_L//2)+(count_R//2+count_R%2)
        count = 0

print(' '.join(map(str,li[:len(S)-1])))