#https://atcoder.jp/contests/abc039/tasks/abc039_c
#頭悪すぎる
S = str(input())
li = [["WBWBWWBWBWBWWBWBWWBW","Do"],["WBWWBWBWBWWBWBWWBWBW","Re"],\
    ["WWBWBWBWWBWBWWBWBWBW","Mi"],["WBWBWBWWBWBWWBWBWBWW","Fa"],\
    ["WBWBWWBWBWWBWBWBWWBW","So"],["WBWWBWBWWBWBWBWWBWBW","La"],\
    ["WWBWBWWBWBWBWWBWBWWB","Si"]]
for i in li:
    if i[0]==S:
        print(i[1])