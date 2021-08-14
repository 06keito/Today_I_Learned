def Combination_array(array,group):
    new_array = []
    for i in array:
        new_array.append([i,group])
    return new_array

def main():
    N,M = map(int,input().split())
    A_array = list(set(map(int,input().split())))
    B_array = list(set(map(int,input().split())))

    array = list(Combination_array(A_array,"A") + Combination_array(B_array,"B"))
    array.sort()
    ans = 10**9

    for i in range(len(array)-1):
        if array[i][1]!=array[i+1][1]:
            ans = min(ans,abs(array[i][0]-array[i+1][0]))
    print(ans)

if __name__ == "__main__":
    main()