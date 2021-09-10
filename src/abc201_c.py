def main():
    S = str(input())
    ans = 0
    for i in range(10000):
        array = [False]*10
        now = i
        for j in range(4):
            array[now%10] = True
            now //= 10
        N = 1
        for j in range(10):
            if (S[j] == "o" and not array[j]) or (S[j] == 'x' and array[j]):
                N = 0
        ans += N
    print(ans)
            

if __name__ == "__main__":
    main()