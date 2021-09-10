import itertools

def main():
    S = input()
    array = [0]*(len(S)+1) # 総和を求めるための配列

    for i in range(len(S)):
        if S[i]=="<": #増加する場合のみ判定する,右方向に見ていくイメージ
            array[i+1] = array[i]+1

    #print(array)
    S,array = S[::-1],array[::-1] #反転させることによって左右から見ていくことになる
    #print(S,array)
    
    for i in range(len(S)):
        if S[i]==">":
            array[i+1] = max(array[i]+1,array[i+1])
    #print(array)
    print(sum(array))
    
if __name__ == "__main__":
    main()