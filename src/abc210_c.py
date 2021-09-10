import collections

def bool_check():
    global flag
    if flag == "True":
        flag = "False"
        return True
    else:
        False

def main():
    N,K = map(int,input().split())
    C = list(map(int,input().split()))
    dict = collections.defaultdict(int)
    ans = 0

    for i,a in enumerate(C):
        dict[a] += 1
        if i>=K:
            dict[C[i-K]]-=1
            if dict[C[i-K]]==0:
                dict.pop(C[i-K])
        if i>=K-1:
            ans = max(ans,len(dict.keys()))
    print(ans)
if __name__ == "__main__":
    flag = "True"
    main()